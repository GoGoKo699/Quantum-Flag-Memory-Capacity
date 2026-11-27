# Scientific account

The decoder receives a nonorthogonal flag for each phase error. It must process those flags before accessing the noisy data. The central result gives the optimal asymptotic rate of logical qubits transmitted at each allowed quantum storage rate across that boundary.

| Question | Scientific account |
| --- | --- |
| What arrives before and after the storage boundary? | [Channel and resources](model.md) |
| How many logical qubits per use are achievable? | [Exact capacity curve](capacity.md) |
| Why can a collective flag compressor do no better? | [Converse and entropy inequality](converse.md) |
| How can the decoder attain the curve? | [Measurement, compression and syndrome decoding](achievability.md) |
| How do finite block lengths change the guarantee? | [Finite blocks](finite-block.md) |
| Which ideas and results does the proof inherit? | [Related work](related-work.md) |

The proof concerns an ideal phase-only channel with fixed independent error probabilities, known pure flags and noiseless processing. Its converse allows arbitrary encoders, joint flag compressors and final decoders under the stated timing and memory constraints.
