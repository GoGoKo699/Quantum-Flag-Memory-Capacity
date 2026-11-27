# Quantum Flag Memory Capacity

**How much quantum memory should a receiver keep while it waits for the error syndrome?** For independent phase errors with nonorthogonal pure-state flags, an exact capacity curve gives the reliable quantum transmission rate at every retained-memory budget. A two-outcome measurement, compression of the residual flag states and syndrome-conditioned correction attain the curve.

The data qubits take a separate path. Before the cut the receiver can jointly process all flag qubits and keep an unlimited classical record plus $`q`$ quantum qubits per channel use. After the cut it receives the noisy data and can extract the syndrome. The model uses calibrated, ideal operations and counts persistent flag memory at the cut.

Let $`f(r)=h_2((1+r)/2)`$, with $`h_2`$ the binary entropy. For phase-error probability $`p`$ and flag overlap $`c`$, put $`x_0=2c\sqrt{p(1-p)}`$ and $`\chi=f(\sqrt{x_0^2+(1-2p)^2})`$.

```math
C(q)=
\begin{cases}
1+q-f\!\left(\sqrt{\bigl[f^{-1}(q)\bigr]^2-x_0^2}\right), & 0\le q\le\chi,\\
1-h_2(p)+\chi, & q\ge\chi .
\end{cases}
```

Here $`C(q)`$ counts logical qubits per channel use at vanishing error. For $`0\lt p,c\lt 1`$, the rate rises strictly up to $`\chi`$, and every interior point improves on time-sharing between the two endpoint receivers.

| Strategy at $`p=1/2`$ and $`c=0.8`$ | Retained flag qubits per use | Logical qubits per use |
| --- | ---: | ---: |
| Measure immediately | $`0`$ | $`0.2781`$ |
| Time-share the endpoint receivers | $`0.20`$ | $`0.3595`$ |
| Tune the measurement and compress the residual | $`0.20`$ | $`0.3803`$ |
| Compress the unmeasured flags | $`0.4690`$ | $`0.4690`$ |

## Read the science

| Question | Scientific account |
| --- | --- |
| What crosses the memory cut? | [Channel, flags and resource model](science/model.md) |
| What is the exact rate? | [Capacity and entropy optimization](science/capacity.md) |
| Why does the upper bound cover joint preprocessing? | [Converse](science/converse.md) |
| How can a receiver attain the curve? | [Measurement, compression and correction](science/achievability.md) |
| What can be checked at finite block length? | [Finite-block resources](science/finite-block.md) and [reproducibility](verification/README.md) |
| Which ingredients come from prior work? | [Related work](science/related-work.md) and [bibliography](references/references.bib) |

## Learn the project

John Watrous’s *The Theory of Quantum Information* (2018) is the educational anchor. The [Watrous bridge](learning/WATROUS_BRIDGE.md) connects the textbook’s channel, measurement, entropy and coding tools to the proof. The [30 milestones](learning/MILESTONES.md) provide a route from the flag model to the full capacity curve. The [reading guide](llms.txt) points to the main results and checks.

## Reproduce the checks

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks verify the detector construction, examples and finite cases. The [written proofs](science/README.md) establish the asymptotic result. The final joint syndrome decoder can be computationally expensive.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
