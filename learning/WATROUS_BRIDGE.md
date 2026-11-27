# From Watrous to capacity with delayed flag readout

A phase error on a data qubit also leaves a pure-state flag. A receiver can measure the flag early for a classical clue and hold part of its quantum state until the code syndrome arrives. The project asks how the amount held across that waiting period changes the rate at which unknown qubits can be transmitted.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The section numbers below follow the author's January 2018 manuscript. [Book page](https://cs.uwaterloo.ca/~watrous/TQI/) · [Contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf)

| Milestones | Anchor sections | What to carry into the project |
| --- | --- | --- |
| M01–M05 | [Chapter 2, §§2.1.2–2.1.3, 2.2.1–2.2.2 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | States and purifications describe the flags and their reference. Positive measurement effects determine branch probabilities, and a Kraus representation describes the residual state. |
| M02, M27 | [Chapter 3, §§3.1.1 and 3.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | The trace norm determines the best binary discrimination probability. The fidelity of the recovered state measures transmission quality when testing a logical input entangled with a reference. |
| M06–M08, M17–M20 | [Chapter 5, §§5.1–5.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Shannon and von Neumann entropy give the two terms in the residual error uncertainty. Relative-entropy data processing underlies the branch information bound. |
| M24–M25 | [Chapter 5, §5.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Quantum source coding stores a long block in a typical spectral subspace at a rate approaching the source entropy. |
| M11–M12, M15–M16 | [Chapter 8, §§8.2.1–8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) | Entanglement transmission defines the task. Coherent information connects quantum transmission to the entropy of the output and reference. |

## Translate the notation

| Textbook concept | Project object | Role |
| --- | --- | --- |
| Pure-state ensemble | Two flags for a Bernoulli phase error | The input to the early flag processor |
| Measurement effect and Kraus operator | $`E_y`$ and $`\sqrt{E_y}`$ | Outcome weight and retained quantum state |
| Purifying register | Error-label reference with transverse coordinate $`x_0`$ | Turns the flag overlap into a constraint on every collection of conditional states |
| Classical–quantum conditional entropy | $`H(X^n\mid YQ)`$ | Residual error uncertainty before the syndrome |
| Coherent information | $`n-H(X^n\mid YQ)`$ at the maximally mixed input | A code rate bound for a fixed block processor |
| Typical subspace | Encoded flag register across the memory cut | The space occupied by the compressed residual flags |

Once the early instrument has run, the noisy block and retained outputs together form the effective channel. Its complementary output can be simulated by reading the output data in the computational basis. This makes the channel degradable. The phase-noise symmetry then makes the maximally mixed input optimal for coherent information. The project proofs connect this textbook language to the timed receiver through a chain-rule reduction and a convex optimization on the qubit reference. [Model](../science/model.md) · [Converse](../science/converse.md)

The achievability proof uses Devetak and Winter's classical source coding with quantum side information. The stabilizer syndrome serves as the bin index for the physical error string. The later decoder also has the classical outcomes and the decompressed flag states. [Devetak and Winter](https://arxiv.org/abs/quant-ph/0209029) · [Achievability](../science/achievability.md)

## Work through one memory setting

Take equally likely phase errors and flag overlap $`c=0.8`$. A convenient choice of flag vectors is

```math
\lvert\psi_x\rangle=\sqrt{0.9}\lvert 0\rangle+(-1)^x\sqrt{0.1}\lvert 1\rangle.
```

The unmeasured average flag has entropy $`h_2(0.9)\simeq 0.469`$ bits. A budget of $`q=0.20`$ qubits per flag lies below that entropy. Write $`f(r)=h_2((1+r)/2)`$. The residual flag states should have an average spectrum with Bloch radius $`r\simeq 0.93775`$, which gives $`f(r)=0.20`$.

In this equal-prior example the transverse coordinate of the project reference is $`c`$. The two branches can have vertical coordinates $`\pm z`$ with $`z=\sqrt{r^2-c^2}\simeq 0.48926`$. Use the two-outcome measurement with effects

```math
E_\pm=\tfrac12(I\pm\kappa X_{\mathrm{flag}}),\qquad
\kappa=\frac{z}{\sqrt{1-c^2}}\simeq 0.81544.
```

Here $`X_{\mathrm{flag}}`$ is the Pauli operator on the flag. Use the positive square roots of these effects as the branch operators. The record has two equiprobable outcomes. Each record narrows the conditional distribution of the error label to one with entropy $`f(z)\simeq 0.81968`$. Each residual ensemble consists of pure states with an average state of entropy $`q`$. Hence this quantum output lowers the residual error uncertainty to $`f(z)-q\simeq 0.61968`$ bits per site.

Compress the residual block after recording the outcome labels. Once the syndrome arrives, asymptotically just over $`0.61968`$ independent binary parity checks per site suffice to decode the physical phase errors. These checks leave a logical rate approaching $`0.38032`$ qubits per site, using continuity and storage slack to satisfy the hard budget. [Achievability](../science/achievability.md)

| Early receiver strategy | Retained qubits per site | Logical qubits per site |
| --- | ---: | ---: |
| Immediate measurement of every flag | 0 | 0.27807 |
| Time-sharing between immediate measurement and full flag information | 0.20 | 0.35949 |
| Two-outcome weak measurement with compressed residual flags | 0.20 | 0.38032 |
| Full flag information using compression | 0.46900 | 0.46900 |

Time-sharing reaches the same memory budget by using the full-information strategy on about $`0.20/0.46900`$ of the sites. The weak measurement uses a small quantum contribution from every site. The strict concavity of the capacity curve gives the better rate at the same storage cost. The comparison concerns asymptotic rates for ideal storage and decoder operations. [Capacity theorem](../science/capacity.md) · [Finite-block resources](../science/finite-block.md)

## Follow the complete route

The [30 milestones](MILESTONES.md) connect this example to the exact capacity for biased error priors. Follow the [converse](../science/converse.md) for the arbitrary joint early processor bound and the [achievability proof](../science/achievability.md) for the attaining instrument and code.
