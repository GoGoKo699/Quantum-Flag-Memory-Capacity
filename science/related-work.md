# Related work

## Coding and compression ingredients

- **Generalized dephasing.** Devetak and Shor obtained a single-letter capacity region for generalized dephasing channels. Fixing the early flag instrument gives a generalized dephasing channel on the entire data block. The [converse](converse.md) shows how Pauli covariance gives its maximum coherent information and then bounds that quantity uniformly over the allowed block instruments. [Devetak and Shor](https://arxiv.org/abs/quant-ph/0311131)
- **Quantum source coding.** Schumacher compression stores the residual flags at the entropy of their average state. In the attaining instrument the two conditional average states have the same spectrum. Rotations selected by the classical outcomes put them in a common basis before compression. [Schumacher](https://doi.org/10.1103/PhysRevA.51.2738)
- **Decoding with quantum side information.** Devetak and Winter proved that a classical source can be compressed to its conditional entropy given quantum side information. Renes and Renner give a one-shot bound using universal hashing. In the [achieving code](achievability.md), the hash is a binary linear parity check so that the receiver can read it as a stabilizer syndrome. The retained flags supply the side information for decoding the error string. [Devetak and Winter](https://doi.org/10.1103/PhysRevA.68.042301) · [Renes and Renner](https://doi.org/10.1109/TIT.2011.2177589)

## Delayed flag measurements

**Quantum Delayed Syndrome Decoder** uses the same pure-state error flags up to a change of Pauli basis. For a fixed binary syndrome matrix whose kernel has dimension $`k`$, its streaming instrument preserves the full flag experiment within each syndrome class using $`k`$ retained qubits. It therefore preserves the optimum for every prior and loss on that class. Here the source has a fixed independent Bernoulli error law and the code can change with the memory budget. The capacity converse covers arbitrary block codes and joint early flag instruments, and the tunable two-outcome instrument attains the intermediate rates. [Delayed linear syndromes](https://github.com/GoGoKo699/Quantum-Delayed-Syndrome-Decoder/blob/f283fb2ef1b9475ce5dd98a3244af06c445ea804/science/linear-syndromes.md)

**Quantum Erasure Flag Compression** gives a monitor the replacement-event label and lets it design a flag for exact recovery. Here the flags are supplied as nonorthogonal quantum states and the compressor has access to those states alone. The data syndrome arrives after the memory cut, and capacity concerns vanishing logical error for a known source law. [Quantum Erasure Flag Compression](https://github.com/GoGoKo699/Quantum-Erasure-Flag-Compression/blob/ad70018eb0a015634b815b88ec321dc63099b70a/README.md)

Savadatti and colleagues certify a coherent processing advantage for a finite sequence of correlated readout pulses. They bound adaptive pulse-by-pulse measurements through a positive-partial-transpose relaxation. The capacity problem here allows a global flag measurement before the syndrome even at zero retained qubits, and prices the persistent quantum register per channel use. [Savadatti et al.](https://arxiv.org/abs/2611.25216)

Han, Leuchs and Grassl quantify the accessible information obtained by an initial measurement and a later measurement of its residual quantum state. In the capacity construction the later decoder also receives the stabilizer syndrome from the data. That additional side information gives operational meaning to the conditional Holevo information of the postmeasurement flags. [Han, Leuchs and Grassl](https://doi.org/10.1103/PhysRevLett.120.160501)

## Source reconstruction and correlation compression

Barnum, Hayden, Jozsa and Winter show that a blind compressor with free classical storage still needs the Schumacher rate to reconstruct an irreducible pure-state source faithfully. Hayden, Jozsa and Winter also characterize visible compression when the encoder receives the state labels. Here the compressor is blind and the task is reliable transmission through the flagged data channel. The memory law specifies the transmission rate at each budget below faithful storage. [Barnum et al.](https://doi.org/10.1098/rspa.2001.0816) · [Hayden, Jozsa and Winter](https://doi.org/10.1063/1.1497184)

Farber and Gour study how classical communication saves quantum storage at fixed single-shot reconstruction error. Wolff and colleagues give worst-case obstructions to small-dimensional compression that preserves quantum mutual information. The capacity formula here concerns a fixed independent binary pure-state ensemble, with free classical output, a hard quantum dimension cap, and access to the data syndrome after compression. [Farber and Gour](https://arxiv.org/abs/2610.14785) · [Wolff et al.](https://arxiv.org/abs/2611.28361)

[BibTeX entries](../references/references.bib)
