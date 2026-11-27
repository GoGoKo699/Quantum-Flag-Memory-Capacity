# Finite blocks and receiver resources

The [capacity theorem](capacity.md) takes the block length to infinity at fixed memory rate. At finite block length, the number of logical qubits, the number of storage qubits, and entanglement infidelity are separate constraints. A finite upper bound and a compression construction make two of the constraints explicit.

## A finite upper bound at any memory budget

Let $`n`$ be the number of data carriers, $`k\ge1`$ the number of logical qubits, and $`d_Q`$ the dimension of the quantum flag register that crosses the cut. Define $`q_n=\log_2(d_Q)/n`$. Let $`\epsilon`$ be the entanglement infidelity for a maximally entangled logical input and reference. Then

```math
k-h_2(\epsilon)-\epsilon\log_2(4^k-1)\le n C(q_n).
```

In particular, for $`\epsilon\lt 1/2`$,

```math
k\le\frac{n C(q_n)+h_2(\epsilon)}{1-2\epsilon}.
```

To see this, average the decoded reference–logical state under conjugate local unitaries $`U\otimes\overline U`$. The resulting state is diagonal in the decomposition into the maximally entangled vector and its orthogonal complement. The two total weights are $`1-\epsilon`$ and $`\epsilon`$, and the orthogonal complement has uniform eigenvalues. The output marginal is maximally mixed. Conditional entropy is concave and invariant under local unitaries, so the decoded state's coherent information is at least that of the averaged state, which is the left-hand side of the first inequality. Data processing and the [block converse](converse.md) give the upper bound.

At a fixed $`n`$, the bound can exclude a target logical payload or error tolerance for a proposed memory register. It applies to arbitrary joint early processing and arbitrary coding in the model.

## Compression with bounded temporary workspace

Consider an interior choice of the [two-outcome receiver instrument](achievability.md) at intrinsic memory rate $`q_*`$. The conditional average residual flag states have the same spectrum $`(1-\theta,\theta)`$, with $`q_*=h_2(\theta)`$ and $`0\lt \theta\lt 1/2`$. For each outcome rotate the residual into its average state's eigenbasis. Conditioned on the classical outcomes, the average of a length-$`m`$ block is then a tensor power with this spectrum.

Choose $`u`$ with $`\theta\lt u\lt 1/2`$. The compressor keeps the subspace of computational basis strings of Hamming weight at most $`\lfloor mu\rfloor`$. Its rank $`D_m`$ and its discarded average weight $`\delta_m`$ satisfy

```math
D_m=\sum_{j=0}^{\lfloor mu\rfloor}\binom mj\le 2^{m h_2(u)},\qquad
\delta_m=\Pr\{\operatorname{Bin}(m,\theta)\gt \lfloor mu\rfloor\}\le
2^{-m D_2(u\Vert\theta)}.
```

Here $`D_2(u\Vert\theta)=u\log_2(u/\theta)+(1-u)\log_2((1-u)/(1-\theta))`$. The dimension bound follows from the probability of the same set under a Bernoulli-$`u`$ product distribution. The probability bound is the binomial Chernoff bound. A basis permutation maps the kept strings into $`\lceil\log_2 D_m\rceil`$ qubits. On a rejected projection outcome the compressor substitutes a fixed state in the same register. The decoder embeds the kept register back into the original space and applies the inverse outcome-conditioned rotations. All trials are counted.

For a pure residual flag state with rejected weight $`e`$, the reconstructed state has overlap at least $`(1-e)^2`$ with the original. Across $`b=\lfloor n/m\rfloor`$ complete blocks the ideal residuals are a conditional product. The overlap with the reconstructed product state is at least $`1-2\sum_{j=1}^b e_j`$. The fidelity–trace-distance bound and concavity of the square root give an average trace distance at most $`\sqrt{2b\delta_m}`$. Here trace distance is one half the trace norm. This quantity also bounds the increase in average decoding error, since it bounds the change in the probabilities of any measurement on the ensemble.

Keep the remaining $`n-bm`$ flags directly. The compressor retains at most $`b\lceil\log_2 D_m\rceil+n-bm`$ qubits at the cut. At fixed slack $`h_2(u)\lt q`$, choosing $`m`$ proportional to $`\log n`$ with a large enough coefficient gives a vanishing compression penalty and cut memory below $`nq`$ for all sufficiently large $`n`$. The early compressor then needs only $`O(\log n)`$ temporary flag qubits in addition to the completed compressed blocks. This width statement uses ideal basis permutations with no bound on their gate counts.

## A finite syndrome decoder

Fix a full-rank binary check matrix $`H`$ with $`n-k`$ rows. Let $`\rho_{x,y}`$ be the retained state for error string $`x`$ and classical record $`y`$, and let $`p(x,y)`$ be their joint probability. For a syndrome $`s=Hx`$, set

```math
A_{x,y}=p(x,y)\rho_{x,y},\qquad
G_{s,y}=\sum_{Hx=s}A_{x,y},\qquad
M_{x|s,y}=G_{s,y}^{-1/2}A_{x,y}G_{s,y}^{-1/2}.
```

The inverse is on the support. The operators $`M_{x|s,y}`$ form a pretty-good measurement there and can be completed arbitrarily on the kernel. Its exact error probability is

```math
\epsilon_{\mathrm{PGM}}=1-\sum_{x,y}\operatorname{Tr}
\bigl(M_{x|Hx,y}A_{x,y}\bigr).
```

Each mistaken label inside the observed syndrome class leaves a nonidentity logical phase Pauli. The code has only $`X`$-type stabilizers, so a nonzero pure $`Z`$ error in the kernel of $`H`$ cannot be a stabilizer. Thus the classical decoding error equals the logical entanglement infidelity for this recovery. A numerical finite-block evaluation can work on the retained register because any decompression can be incorporated into the decoder's measurement.

Direct evaluation requires considering $`2^k`$ error strings per syndrome and inverting a matrix of dimension up to $`d_Q`$ for each relevant classical record and syndrome. The one-flag instrument and logarithmic temporary compression width therefore leave a separate decoding-complexity question. The capacity proof guarantees asymptotic performance with suitable checks. The finite inequalities give a bound on a given design and a controlled compression penalty, while the short-block gain of a computationally efficient syndrome decoder remains open.
