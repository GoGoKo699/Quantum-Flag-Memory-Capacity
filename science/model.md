# Channel and resources

## Phase errors with a separate flag

One use consists of a data qubit and a flag. A classical bit $`X`$ equals one with probability $`p`$. The channel applies the Pauli phase error $`Z^X`$ to the data and produces the flag state $`|\psi_X\rangle`$. The two known pure flag states have overlap $`c=|\langle\psi_0|\psi_1\rangle|`$. Here $`0\lt p\lt 1`$ and $`0\lt c\lt 1`$ are fixed. Up to basis and phase conventions the flag states are

```math
|\psi_x\rangle=
\sqrt{\frac{1+c}{2}}|0\rangle
+(-1)^x\sqrt{\frac{1-c}{2}}|1\rangle .
```

On $`n`$ uses the errors $`X^n`$ are independent and identically distributed. Conditional on the error string $`x`$, the data receive $`Z^x=\bigotimes_i Z^{x_i}`$ and the flags are in $`|\psi_x\rangle=\bigotimes_i|\psi_{x_i}\rangle`$. The error process is independent of the input, including any reference entangled with the input. The receiver learns about the error from the supplied flag states and the later data.

## Timing and memory

The sender may encode a logical system into all $`n`$ data qubits using any quantum channel. The receiver first applies an instrument to the $`n`$ flags. All flags may be processed jointly. The instrument produces a classical record $`Y`$ and a quantum system $`Q`$ satisfying

```math
\log_2 \dim Q\le \lfloor nq\rfloor .
```

This dimension counts all retained quantum systems under the control of the flag processor across the boundary. Previously retained ancillary quantum systems count toward the same dimension. There is no preshared entanglement. Classical storage is free.

The noisy data are held separately and become accessible to the decoder together with $`YQ`$ after the boundary. The flag processor has no earlier access to the data or a data-derived syndrome. It knows the phase-error probability and both possible flag states. The final decoder may act jointly on all resources it receives.

| Resource | Convention |
| --- | --- |
| Channel uses | One noisy data qubit and one supplied pure flag each |
| Sustained quantum flag memory | $`\lfloor nq\rfloor`$ qubits at the boundary |
| Classical records | Unrestricted across the boundary |
| Temporary workspace | Ideal and unrestricted within each side of the boundary |
| Data and flag operations | Noiseless implementation of the selected encoder, receiver and decoder |
| Additional quantum resources | No preshared entanglement or extra flag path across the boundary |

This model prices the persistent flag record at one specified boundary. Peak circuit width, flag arrival rate, storage noise, syndrome extraction error and decoding runtime are separate resources.

## Rate criterion

A code carries $`k_n`$ logical qubits. Test it by sharing a maximally entangled state between those qubits and a reference, applying the physical channel and recovering the logical output. The entanglement infidelity is one minus the overlap of the recovered joint state with that maximally entangled state. A rate is achievable if there is a sequence of codes whose entanglement infidelity tends to zero and whose limiting lower rate is at least that rate. Capacity is the supremum of achievable rates.

The explicit phase-correction code also protects arbitrary logical inputs, including those entangled with a reference. Its ideal correction fails with a probability independent of the input. Compression changes this failure probability by an amount tending to zero.
