# Exact capacity curve

Let $`h_2`$ be binary entropy in bits and write $`f(r)=h_2((1+r)/2)`$ for $`0\le r\le1`$. Use the decreasing branch of its inverse. Define

```math
x_0 = 2c\sqrt{p(1-p)},\qquad
z_0 = 1-2p,\qquad
r_0 = \sqrt{x_0^2+z_0^2},\qquad
\chi = f(r_0).
```

The flag ensemble has average state $`(1-p)|\psi_0\rangle\langle\psi_0|+p|\psi_1\rangle\langle\psi_1|`$ with entropy $`\chi`$. In the [channel model](model.md), the exact capacity in logical qubits per channel use is

```math
C(q)=
\begin{cases}
1+q-f\!\left(\sqrt{f^{-1}(q)^2-x_0^2}\right), & 0\le q\le\chi,\\
1-h_2(p)+\chi, & q\ge\chi .
\end{cases}
```

The two cases agree because $`f^{-1}(\chi)=r_0`$ and $`f(|z_0|)=h_2(p)`$. This is an asymptotic theorem at fixed $`p,c,q`$. The [converse](converse.md) bounds every allowed receiver, while the [construction](achievability.md) uses an independent two-outcome instrument on each flag, quantum source compression and a linear stabilizer syndrome.

## Strict gain below the full-storage rate

Set $`r=f^{-1}(q)`$ and $`z=\sqrt{r^2-x_0^2}`$. For $`0\lt q\lt \chi`$,

```math
C'(q)=1-\frac{A(z)}{A(r)},\qquad A(u)=\frac{\mathrm{atanh}u}{u},\qquad A(0)=1.
```

The function $`A`$ is strictly increasing. Since $`r\gt z`$, the derivative is positive. The function $`v\mapsto\log A(\sqrt v)`$ is strictly convex on $`[0,1)`$ by its integral representation $`A(\sqrt v)=\int_0^1 (1-vt^2)^{-1}\,dt`$ and Hölder's inequality. With $`r^2=z^2+x_0^2`$ this makes the ratio $`A(z)/A(r)`$ strictly increase as $`q`$ increases. Thus $`C`$ is strictly concave below $`\chi`$ and exceeds the straight line from immediate measurement to full-rate storage. The smallest memory rate attaining the unrestricted capacity is exactly $`\chi`$.

For uniform phase errors, the capacity with no quantum flag storage is $`1-h_2((1-\sqrt{1-c^2})/2)`$. The attaining receiver is the Helstrom measurement followed by a phase-error-correcting stabilizer code. At full storage the capacity in this uniform case is $`h_2((1+c)/2)`$.

## Worked setting

For $`p=0.5`$ and $`c=0.8`$ the flag entropy is about $`0.4690`$ qubits per use. At a memory budget $`q=0.20`$ the optimized instrument has strength about $`0.8154`$ when strength zero denotes the identity branch and strength one denotes the Helstrom measurement.

| Strategy | Persistent flag qubits per use | Logical qubits per use |
| --- | ---: | ---: |
| Immediate measurement | 0 | 0.2781 |
| Time-sharing at the same memory budget | 0.20 | 0.3595 |
| Optimized weak instrument | 0.20 | 0.3803 |
| Full coherent rate | 0.4690 | 0.4690 |

The [finite-block account](finite-block.md) quantifies the effects of approximating the asymptotic construction at finite length.
