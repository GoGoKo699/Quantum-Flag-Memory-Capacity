# Converse for arbitrary flag instruments

Fix a block of $`n`$ uses and an arbitrary early instrument. Write $`\tau_x`$ for its output on the product flag for error string $`x`$. It includes the classical register $`Y`$ and the persistent quantum system $`Q`$. The resulting channel from the physical input to the final receiver is

```math
\mathcal N(\rho)=\sum_x p_x Z^x\rho Z^x\otimes\tau_x .
```

The proof first reduces optimal quantum transmission for this fixed instrument to conditional entropy of the errors. It then bounds that entropy for every instrument with the allowed memory dimension.

It suffices to consider finite classical records for coding. At fixed block length the final decoder conditioned on each record is a channel between finite-dimensional systems. Approximate this family to accuracy $`\epsilon`$ in diamond norm by a finite channel net, then store the selected decoder index as the coarsened record. This changes the final decoded state by at most $`\epsilon`$ in trace norm and keeps the same quantum memory dimension. Taking arbitrarily fine nets extends the bound to general record spaces.

## Reduce coding to conditional phase entropy

Let $`|\eta_x\rangle`$ purify $`\tau_x`$ and append an orthogonal environment label $`|x\rangle`$ in a Stinespring dilation. On a computational-basis input $`|j\rangle`$ the joint output is

```math
|j\rangle\otimes\sum_x \sqrt{p_x}(-1)^{j\cdot x}|\eta_x\rangle|x\rangle .
```

Tracing out the data discards every off-diagonal input matrix entry. Measuring the output data in the computational basis therefore gives precisely the distribution needed to prepare the complementary output. This is a degrading channel, so the coherent information is concave in the input. Conjugating the input by a tensor product of Pauli operators conjugates the data output by the same Pauli. In the displayed dilation the complement changes by at most an environment unitary on the label register. Hence coherent information is invariant under Pauli conjugation. Twirling shows that the maximally mixed input achieves its maximum.

The channel acting on half a maximally entangled state makes orthogonal Bell states indexed by $`x`$. The conditional entropy identity gives

```math
\max_\rho I_{\mathrm c}(\rho,\mathcal N)=n-H(X^n|YQ).
```

This follows directly by subtracting $`H(X^n)+\sum_x p_x S(\tau_x)`$ from $`n+S(\sum_x p_x\tau_x)`$.

For arbitrary CPTP encoding, let $`L`$ be the logical reference and let $`\sigma_{LA}`$ be the encoded reference–input state, which can be mixed. The function $`-S(L|B)`$ after the noisy channel is convex in $`\sigma_{LA}`$ by concavity of conditional entropy. A pure-state decomposition of $`\sigma_{LA}`$ therefore bounds it above by the maximum coherent information over physical input states. Data processing under the final decoder can only decrease coherent information. For a code carrying $`k`$ logical qubits with vanishing entanglement infidelity, continuity of $`S(L|B)`$ on the $`2^k`$-dimensional reference bounds the final coherent information below by $`k-o(k)-o(1)`$. Dividing by $`n`$ yields the required achievable-rate bound from the fixed-instrument coherent information. The continuity argument also bounds $`k=O(n)`$ for any reliable sequence.

## Reduce a collective instrument to one-flag branches

Write $`M=I(X^n;Q|Y)`$. For a classical error label, Holevo information gives $`M\le\log_2\dim Q`$. The chain rules read

```math
H(X^n|Y)=\sum_{i=1}^n H(X_i|Y,X_{\lt i}),\qquad
M=\sum_{i=1}^n I(X_i;Q|Y,X_{\lt i}).
```

Fix a site and a value of $`X_{\lt i}`$. In the original collective instrument insert the corresponding known earlier flag states, and insert the average flag state at each later site. Independence makes this a valid single-flag instrument realizing exactly the conditional state at the current site.

Let $`E_y`$ be the effects of that single-flag instrument. The branch with outcome $`y`$ can be realized by first applying $`\sqrt{E_y}`$ and then applying a channel to the residual state. To see this, write the original branch Kraus operators as $`K_{y,a}=K_{y,a}E_y^{-1/2}\sqrt{E_y}`$, using the inverse on the support. The operators $`K_{y,a}E_y^{-1/2}`$ have squares summing to the support projection. A completion to a channel outside that support leaves the branch statistics unchanged.

Use a reference that purifies the average flag state by attaching basis states $`|0\rangle,|1\rangle`$ to the two possible flags. Its Bloch vector is $`(x_0,0,z_0)`$. After the Lüders operation $`\sqrt{E_y}`$, denote the normalized reference state by $`\rho_y`$ and its branch probability by $`p_y`$. The average $`\sum_y p_y\rho_y`$ is the initial reference state. In this canonical branch the joint flag–reference state is pure. Thus its residual conditional Holevo information is $`S(\rho_y)`$, while its uncertainty about the classical bit is $`S(\Delta\rho_y)`$, where $`\Delta`$ dephases in the label basis. The original branch has the same classical bit uncertainty and at most this much quantum conditional information by data processing.

Now average over all sites, earlier label values and branch outcomes. Put $`T=\mathbb{E}S(\rho_y)`$ for this average. The mean reference state still has Bloch vector $`(x_0,0,z_0)`$, so concavity gives $`T\le\chi`$. The preceding reduction gives $`M/n\le T`$.

## Optimize the two entropies

For a reference qubit with entropy $`t=f(r)`$ and first Bloch coordinate $`x`$, its absolute third coordinate is at most $`\sqrt{r^2-x^2}`$. Its entropy after label dephasing is therefore at least

```math
F(x,t)=f\!\left(\sqrt{f^{-1}(t)^2-x^2}\right).
```

This function is jointly convex and is increasing in $`t`$. It follows by Jensen's inequality that

```math
\frac{H(X^n|Y)}{n}=\mathbb{E}S(\Delta\rho_y)
\ \ge\ F(x_0,T)
\ \ge\ F(x_0,M/n).
```

Consequently the fixed-instrument coherent information per use is at most $`1+M/n-F(x_0,M/n)`$. The bound is increasing in $`M/n`$ up to $`\chi`$ by the derivative calculation in the [capacity theorem](capacity.md). Using $`M/n\le\min(q,\chi)`$ proves the converse.

### Convexity calculation

Use natural logarithms for this calculation, replacing $`f`$ by $`h=\ln(2)f`$ and measuring both entropy variables in nats. This only rescales the input and output entropy coordinates of $`F`$. Set $`r=h^{-1}(t)`$ and $`z=\sqrt{r^2-x^2}`$. Write $`A(u)=\mathrm{atanh}(u)/u`$ and $`K(u)=A'(u)/u`$, extended to zero by continuity. In the interior,

```math
F_t=\frac{A(z)}{A(r)},\qquad
F_{xx}=A(z)-x^2K(z),\qquad
F_{xt}=-\frac{xK(z)}{A(r)},\qquad
F_{tt}=\frac{A(z)K(r)-K(z)A(r)}{A(r)^3}.
```

Positivity of $`A`$ proves monotonicity. The identity

```math
A(z)-(1-z^2)K(z)=\frac{\mathrm{atanh}(z)-z}{z^3}
```

and $`x^2\le 1-z^2`$ imply $`F_{xx}\gt 0`$. The sign of the Hessian determinant is the sign of $`J(z)-J(r)`$ for

```math
J(u)=u^2+\frac{A(u)}{K(u)}=\frac{1}{(1-u^2)K(u)}.
```

The second equality follows from $`A(u)+u^2K(u)=1/(1-u^2)`$. The power series for $`(1-u^2)K(u)`$ has constant term $`2/3`$ and strictly positive higher coefficients in $`u^2`$. Thus $`J`$ is decreasing and $`z\le r`$ proves positive semidefiniteness. The domain $`|x|\le1`$ and $`0\le t\le h(|x|)`$ is convex by concavity of binary entropy. Continuity extends convexity and monotonicity to its boundary.
