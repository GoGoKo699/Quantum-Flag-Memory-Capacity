"""Run the numerical checks for flag-memory capacity and compression."""

import math

import numpy as np


def entropy(probabilities):
    return -sum(float(p) * math.log2(float(p)) for p in probabilities if p > 1e-14)


def binary_entropy(p):
    return entropy([p, 1 - p])


def bloch_entropy(radius):
    return binary_entropy((1 + radius) / 2)


def inverse_bloch_entropy(target):
    if target <= 1e-14:
        return 1.0
    low, high = 0.0, 1.0
    for _ in range(56):
        midpoint = (low + high) / 2
        if bloch_entropy(midpoint) > target:
            low = midpoint
        else:
            high = midpoint
    return (low + high) / 2


def state_entropy(matrix):
    eigenvalues = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2)
    return max(0.0, entropy(eigenvalues))


def flag_parameters(p, c):
    transverse = 2 * math.sqrt(p * (1 - p)) * c
    longitudinal = 1 - 2 * p
    full_memory = bloch_entropy(math.hypot(transverse, longitudinal))
    return transverse, longitudinal, full_memory


def frontier(p, c, memory):
    transverse, _, full_memory = flag_parameters(p, c)
    if memory >= full_memory:
        return 1 - binary_entropy(p) + full_memory
    radius = inverse_bloch_entropy(memory)
    return 1 - bloch_entropy(math.sqrt(radius**2 - transverse**2)) + memory


def flag_amplitudes(p, c, size):
    plus = math.sqrt((1 + c) / 2)
    minus = math.sqrt((1 - c) / 2)
    weighted_flags = np.array([[plus, plus], [minus, -minus]]) @ np.diag(np.sqrt([1 - p, p]))
    tensor = weighted_flags
    for _ in range(size - 1):
        tensor = np.kron(tensor, weighted_flags)
    return tensor


def check_optimal_effects(p, c, memory):
    amplitudes = flag_amplitudes(p, c, 1)
    inverse = np.linalg.inv(amplitudes)
    transverse, longitudinal, _ = flag_parameters(p, c)
    radius = inverse_bloch_entropy(memory)
    posterior_z = math.sqrt(radius**2 - transverse**2)
    effects = np.zeros((2, 2))
    diagonal_entropy, flag_entropy, max_error = 0.0, 0.0, 0.0
    for sign in [1, -1]:
        weight = (1 + sign * longitudinal / posterior_z) / 2
        target = np.array([[1 + sign * posterior_z, transverse],
                           [transverse, 1 - sign * posterior_z]]) / 2
        effect = inverse.conj().T @ (weight * target.T) @ inverse
        assert np.min(np.linalg.eigvalsh(effect)) >= -1e-12
        effects += effect
        reference = (amplitudes.conj().T @ effect @ amplitudes).T / weight
        max_error = max(max_error, float(np.max(np.abs(reference - target))))
        diagonal_entropy += weight * entropy(np.diag(reference))
        flag_entropy += weight * state_entropy(reference)
    return max(
        max_error,
        float(np.max(np.abs(effects - np.eye(2)))),
        abs(flag_entropy - memory),
        abs(1 - diagonal_entropy + flag_entropy - frontier(p, c, memory)),
    )


def check_random_instrument(amplitudes, p, c, quantum_dim, outcomes, hidden_dim, rng):
    size = (amplitudes.shape[0]).bit_length() - 1
    shape = (outcomes * hidden_dim * quantum_dim, amplitudes.shape[0])
    matrix = rng.normal(size=shape) + 1j * rng.normal(size=shape)
    isometry, _ = np.linalg.qr(matrix)
    branches = (isometry @ amplitudes).reshape(outcomes, hidden_dim, quantum_dim, -1)
    diagonal_entropy, flag_information = 0.0, 0.0
    for branch in branches:
        ensemble = np.einsum("hqj,hrj->jqr", branch, branch.conj())
        weights = np.trace(ensemble, axis1=1, axis2=2).real
        probability = sum(weights)
        diagonal_entropy += probability * entropy(weights / probability)
        flag_information += probability * state_entropy(ensemble.sum(axis=0) / probability)
        flag_information -= sum(
            weight * state_entropy(state / weight)
            for weight, state in zip(weights, ensemble)
            if weight > 0
        )
    rate = 1 - (diagonal_entropy - flag_information) / size
    information_bound = frontier(p, c, max(0, flag_information) / size)
    memory_bound = frontier(p, c, math.log2(quantum_dim) / size)
    return rate - min(information_bound, memory_bound)


def check_binomial_bounds():
    cases = 0
    for theta in [.03, .11, .2]:
        for cutoff in [.22, .35, .45]:
            divergence = (cutoff * math.log2(cutoff / theta)
                          + (1 - cutoff) * math.log2((1 - cutoff) / (1 - theta)))
            for block_size in [4, 13, 50, 100]:
                max_weight = math.floor(block_size * cutoff)
                rank = sum(math.comb(block_size, weight) for weight in range(max_weight + 1))
                tail = sum(
                    math.comb(block_size, weight) * theta**weight * (1 - theta)**(block_size - weight)
                    for weight in range(max_weight + 1, block_size + 1)
                )
                assert rank <= 2**(block_size * binary_entropy(cutoff))
                assert tail <= 2**(-block_size * divergence)
                cases += 1
    return cases


def main():
    rng = np.random.default_rng(2726)
    effect_error, excess = 0.0, 0.0
    effect_cases, instrument_cases = 0, 0
    for p in [.11, .31, .5, .77, .97]:
        for c in [.13, .4, .8, .99]:
            _, _, full_memory = flag_parameters(p, c)
            for fraction in [0, .01, .25, .5, .95]:
                effect_error = max(effect_error, check_optimal_effects(p, c, full_memory * fraction))
                effect_cases += 1
            for size, quantum_dim, outcomes, hidden_dim in [
                (1, 1, 3, 1), (1, 2, 4, 1), (2, 1, 7, 1),
                (2, 2, 4, 1), (3, 2, 5, 1), (3, 2, 3, 2),
            ]:
                amplitudes = flag_amplitudes(p, c, size)
                for _ in range(14):
                    gap = check_random_instrument(amplitudes, p, c, quantum_dim,
                                                  outcomes, hidden_dim, rng)
                    excess = max(excess, gap)
                    instrument_cases += 1
    assert effect_error < 1e-9
    assert excess < 2e-10
    print(f"{effect_cases} optimal POVMs: maximum identity error {effect_error:.3g}")
    print(f"{instrument_cases} sampled instruments on up to three flags: "
          f"maximum excess above the bound {excess:.3g}")
    print(f"{check_binomial_bounds()} finite subspace and binomial tail checks")

    p, c, memory = .5, .8, .2
    _, _, full_memory = flag_parameters(p, c)
    immediate = frontier(p, c, 0)
    rate = frontier(p, c, memory)
    full = frontier(p, c, full_memory)
    time_sharing = immediate + memory / full_memory * (full - immediate)
    assert rate > time_sharing > immediate
    print(f"Example at p={p}, c={c}, q={memory}: rate {rate:.9f}, "
          f"time-sharing {time_sharing:.9f}, immediate {immediate:.9f}, "
          f"full {full:.9f} at q={full_memory:.9f}")


if __name__ == "__main__":
    main()
