# An attaining receiver

The receiver implements a tunable two-outcome measurement, keeps the outcome and compresses the quantum residual. After the storage boundary it learns a stabilizer syndrome from the data, decodes the complete phase error from the syndrome and residual flags, and corrects the data.

## Tune the measurement to the storage rate

Use a target compression rate $`t`$ strictly between zero and $`\chi`$. Put $`r=f^{-1}(t)`$ and $`z=\sqrt{r^2-x_0^2}`$. The condition $`r\gt r_0`$ gives $`z\gt |z_0|`$. Define the trace-one conditional reference states and weights

```math
\rho_\pm=\frac{I+x_0\sigma_x\pm z\sigma_z}{2},\qquad
w_\pm=\frac{1\pm z_0/z}{2}.
```

Both states have entropy $`t`$ and dephased entropy $`f(z)`$. Their average has the required Bloch vector $`(x_0,0,z_0)`$. Let $`B`$ have columns $`\sqrt{1-p}|\psi_0\rangle`$ and $`\sqrt p|\psi_1\rangle`$ in the flag basis. Because $`p,c`$ are in their stated interior ranges, $`B`$ is invertible. Use effects

```math
E_\pm=(B^\dagger)^{-1} w_\pm\rho_\pm^{\mathsf T} B^{-1}
```

and apply the single Kraus operator $`\sqrt{E_\pm}`$ in each branch. The unnormalized reference output is $`(B^\dagger E_\pm B)^{\mathsf T}=w_\pm\rho_\pm`$. Positivity is immediate and the effects sum to the identity because $`\sum_\pm w_\pm\rho_\pm=(B^\dagger B)^{\mathsf T}`$.

For $`p=1/2`$ in the symmetric flag basis of the [channel model](model.md), this simplifies to

```math
E_\pm=\tfrac12(I\pm\kappa\sigma_x),\qquad
\kappa=\frac{z}{\sqrt{1-c^2}}.
```

At $`t=0`$ the effects are rank one and the quantum residual can be discarded. At $`t=\chi`$ the identity instrument keeps the entire flag ensemble accessible before source compression.

## Compress the quantum residual

Conditional on either classical outcome, the residual flag ensemble consists of pure states. Its averaged density operator has the same spectrum as $`\rho_\pm`$ because their joint purification is pure. Outcome-dependent single-qubit rotations put both averaged states into the same eigenbasis with the same eigenvalue order. Schumacher compression then applies to an independent source with entropy $`t`$. The receiver keeps the measured outcomes in a free classical record for inverse rotations after decompression.

If the allowed storage rate is $`q\gt 0`$, choose $`t\lt \min(q,\chi)`$ and a fixed compression slack small enough to fit $`\lfloor nq\rfloor`$ qubits for large $`n`$. The compression and decompression preserve the quantum residual ensemble, together with the classical outcomes and error labels, in average trace distance tending to zero. This follows from high typical-subspace weight and the gentle measurement bound, or from entanglement fidelity for the average state and data processing on a purification. Taking $`t\uparrow\min(q,\chi)`$ after the asymptotic coding bound attains capacity at the exact memory constraint, including $`q=\chi`$. For $`q\gt \chi`$ one may also compress the original ensemble using rate slack.

## Correct phase errors using a linear syndrome

Let $`F`$ denote the uncompressed residual of one flag and $`Y`$ its classical outcome. The entropy of the error bit given both is

```math
H(X|YF)=H(X|Y)-I(X;F|Y)=f(z)-t .
```

Choose a binary parity-check matrix $`H`$ with $`m`$ rows and use the quantum code stabilized by the $`X`$-type Pauli strings given by those rows. Each row checks the parity of the physical $`Z`$ error it anticommutes with. The stabilizer outcomes on an encoded state therefore give exactly $`Hx`$, independent of the logical state. The code has at least $`n-m`$ logical qubits.

Classical source coding with quantum side information can recover $`X^n`$ from a bin index at any asymptotic rate above $`H(X|YF)`$. The random binning can use binary linear maps. For a uniformly sampled binary matrix with $`m`$ rows, distinct strings have collision probability $`2^{-m}`$. This is the two-universal property used in the cq random binning theorem. A decoder conditions on the syndrome and classical outcomes and uses a collective measurement on the decompressed residuals to distinguish compatible strings. A fixed parity-check matrix and its associated decoder attain vanishing average error at each rate strictly above the conditional entropy. [Source coding with quantum side information](https://arxiv.org/abs/1008.0452)

The receiver applies $`Z^{\hat x}`$ when the decoder outputs $`\hat x`$. An exact estimate undoes the error on the full encoded state. A wrong estimate leaves a residual phase error, so the probability of misidentification upper bounds the half-diamond distance of the logical channel from the identity. Compression adds at most its average trace-distance error to the failure probability. With $`m/n`$ tending to $`f(z)-t`$ from above, the achieved logical rate tends to $`1+t-f(z)`$.

| Step | Main asymptotic resources per use |
| --- | --- |
| Flag measurement | One independent two-outcome instrument and one unrestricted classical bit |
| Persistent quantum record | At most $`q`$ flag qubits across the boundary |
| Syndrome | $`f(z)-t`$ binary checks per use, up to coding slack |
| Logical rate | $`1+t-f(z)`$ per use, up to coding slack |

The compression and final cq measurement are block operations. The rate theorem allows their temporary workspace and runtime. The [finite-block account](finite-block.md) records what one can certify about finite-length instances separately from these asymptotic resources.
