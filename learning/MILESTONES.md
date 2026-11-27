# Project understanding map

The first 12 milestones build the phase-error channel and the timed memory problem. The next 18 connect the block converse, the entropy optimizer and the receiver to the complete capacity result. The split leaves room to follow both halves of the proof from their local operations to their common rate.

The educational anchor is John Watrous’s *The Theory of Quantum Information*. The [Watrous bridge](WATROUS_BRIDGE.md) translates its notation and works through one receiver setting.

| Phase | Milestones | Connection |
| --- | --- | --- |
| Background and preliminaries | [M01](#m01-a-phase-error-on-the-payload)–[M06](#m06-binary-entropy-from-a-qubit-radius) | Phase errors, pure flags, instruments and qubit entropy |
| Background and preliminaries | [M07](#m07-information-in-classical-and-quantum-registers)–[M12](#m12-two-routes-to-the-capacity) | Information, syndrome timing, memory and reliable transmission |
| Narrative and innovation | [M13](#m13-the-effective-channel-for-one-block)–[M18](#m18-a-canonical-branch-for-each-effect) | Effective channels and one-site reductions |
| Narrative and innovation | [M19](#m19-the-entropy-envelope-in-bloch-coordinates)–[M24](#m24-aligning-and-compressing-residual-states) | The entropy envelope and the two-outcome instrument |
| Narrative and innovation | [M25](#m25-meeting-a-hard-memory-budget)–[M30](#m30-the-memorycapacity-statement) | Compression, error correction, finite resources and synthesis |

## Phase I. Background and preliminaries

### M01 A phase error on the payload

**Central question.** How does one hidden phase flip affect an unknown data qubit?

**Understanding target.** Follow Pauli $`Z`$ on a superposition and on a qubit entangled with a reference. Keep track of the data state and the classical error label $`X`$ as distinct objects.

**Prerequisites.** None within this map.

**Conceptual connection.** The syndrome later supplies information about $`X`$ while the decoder protects the data's quantum state.

**Canonical sources.** [Model](../science/model.md) · [Watrous §2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M02 Two flags with nonzero overlap

**Central question.** What evidence about the error is present in a single flag?

**Understanding target.** Write the two pure flags in the symmetric basis and compute their overlap $`c`$ from the squared amplitudes.

**Prerequisites.** [M01](#m01-a-phase-error-on-the-payload).

**Conceptual connection.** The sign of a relative amplitude carries the evidence. Two states with nonzero overlap cannot be distinguished without error.

**Canonical sources.** [Model](../science/model.md) · [Watrous §3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M03 Independent errors across a block

**Central question.** How do the one-site assumptions determine a block channel?

**Understanding target.** For a fixed error string, form the tensor product of its flags and multiply the Bernoulli probabilities. Average over the error strings to obtain the mixed data and flag state.

**Prerequisites.** [M01](#m01-a-phase-error-on-the-payload), [M02](#m02-two-flags-with-nonzero-overlap).

**Conceptual connection.** Conditional product states let the converse average over future flags while keeping the current input variable.

**Canonical sources.** [Model](../science/model.md) · [Watrous §2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M04 A reference for the flag ensemble

**Central question.** How does a purification encode the two prior weights and their overlap?

**Understanding target.** Purify the average flag by attaching a qubit with the two error labels as basis vectors. Compute the reduced reference state and identify its diagonal and off-diagonal entries.

**Prerequisites.** [M02](#m02-two-flags-with-nonzero-overlap).

**Conceptual connection.** The prior determines the reference's vertical Bloch coordinate and the overlap sets its transverse coordinate.

**Canonical sources.** [Model](../science/model.md) · [Watrous §2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M05 A measurement with residual state

**Central question.** What remains after an outcome has been recorded?

**Understanding target.** Use an effect $`E_y`$ and its positive square root to compute the outcome probability and the normalized residual state. Check the completeness condition for the instrument.

**Prerequisites.** [M02](#m02-two-flags-with-nonzero-overlap), [M04](#m04-a-reference-for-the-flag-ensemble).

**Conceptual connection.** The same outcome can be retained in a classical register while its conditional quantum state travels to the memory.

**Canonical sources.** [Model](../science/model.md) · [Watrous §2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M06 Binary entropy from a qubit radius

**Central question.** How do the reference's spectrum and its diagonal give different entropies?

**Understanding target.** Evaluate $`f(r)=h_2((1+r)/2)`$ for the Bloch radius $`r`$ and $`f(z)`$ for its vertical coordinate $`z`$.

**Prerequisites.** [M04](#m04-a-reference-for-the-flag-ensemble).

**Conceptual connection.** The geometric gap between radius and vertical coordinate controls the quantum information retained after a weak flag measurement.

**Canonical sources.** [Capacity theorem](../science/capacity.md) · [Watrous §5.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M07 Information in classical and quantum registers

**Central question.** How do the outcome and residual state each contribute information about the flag label?

**Understanding target.** Expand $`I(X;YQ)`$ using the chain rule. Give the conditional Holevo-information expression for $`I(X;Q\mid Y)`$.

**Prerequisites.** [M05](#m05-a-measurement-with-residual-state), [M06](#m06-binary-entropy-from-a-qubit-radius).

**Conceptual connection.** The receiver has two forms of side information with separate storage costs.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §5.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M08 A dimension bound at the memory cut

**Central question.** Why can a $`d`$-dimensional held register contribute at most $`\log_2 d`$ bits about the classical label beyond the outcomes?

**Understanding target.** Bound the entropy of each averaged conditional state by $`\log_2 d`$ and use nonnegativity of the conditional state entropies.

**Prerequisites.** [M07](#m07-information-in-classical-and-quantum-registers).

**Conceptual connection.** The budget is the actual quantum dimension through the waiting period. The flag instrument may produce any classical record.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §5.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M09 Parity checks from commuting stabilizers

**Central question.** How does a code reveal a binary hash of an unknown phase error?

**Understanding target.** Use Pauli anticommutation to derive the syndrome $`Hx`$ from commuting $`X`$-type checks. Explain why a codeword acquires only the new stabilizer eigenvalues under a phase error.

**Prerequisites.** [M01](#m01-a-phase-error-on-the-payload), [M03](#m03-independent-errors-across-a-block).

**Conceptual connection.** The syndrome supplies a classical bin label for a later quantum decision about the error string.

**Canonical sources.** [Achievability](../science/achievability.md).

### M10 The order of access

**Central question.** At what point can the receiver use the noisy data and the syndrome?

**Understanding target.** List the inputs, outputs and allowed operations before the memory cut, at the cut and after it. Express the quantum budget as a dimension bound on the held flag register.

**Prerequisites.** [M05](#m05-a-measurement-with-residual-state), [M08](#m08-a-dimension-bound-at-the-memory-cut), [M09](#m09-parity-checks-from-commuting-stabilizers).

**Conceptual connection.** The timing rule fixes which information may influence the early instrument. A late measurement may depend on the data and on all retained outputs.

**Canonical sources.** [Model](../science/model.md).

### M11 A rate for protecting unknown data

**Central question.** How is a memory budget turned into a communication problem?

**Understanding target.** Define the logical rate $`k/n`$, the persistent memory rate $`q`$ and vanishing entanglement infidelity. Explain the meaning of a code operating on half a maximally entangled state.

**Prerequisites.** [M01](#m01-a-phase-error-on-the-payload), [M08](#m08-a-dimension-bound-at-the-memory-cut), [M10](#m10-the-order-of-access).

**Conceptual connection.** The limiting task admits encoder and decoder choices for each block size under the same memory budget per channel use.

**Canonical sources.** [Model](../science/model.md) · [Watrous §8.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf).

### M12 Two routes to the capacity

**Central question.** What must be shown to identify the best rate under this timing rule?

**Understanding target.** Specify the required upper bound over block instruments and codes, and the required recovery protocol with vanishing error at the matching rate.

**Prerequisites.** [M07](#m07-information-in-classical-and-quantum-registers), [M09](#m09-parity-checks-from-commuting-stabilizers), [M10](#m10-the-order-of-access), [M11](#m11-a-rate-for-protecting-unknown-data).

**Conceptual connection.** This combines the channel, the timing and the code into the operational quantity that the next phase evaluates.

**Canonical sources.** [Capacity theorem](../science/capacity.md) · [Watrous §8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf).

## Phase II. Narrative and innovation

### M13 The effective channel for one block

**Central question.** What channel remains after a general early flag processor has been fixed?

**Understanding target.** Write the phase-error mixture with the processed output $`\tau_x`$ conditioned on each error string. Keep the input density operator separate from the ensemble of processed states.

**Prerequisites.** [M03](#m03-independent-errors-across-a-block), [M10](#m10-the-order-of-access), [M12](#m12-two-routes-to-the-capacity).

**Conceptual connection.** This turns each possible flag processor into a channel to which a coding converse can be applied.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §2.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M14 Degrading to the environment

**Central question.** Why can the channel output simulate its complement?

**Understanding target.** Use an environment register containing the error labels to construct an isometry. Trace out the data output, and show that measuring the output data in its computational basis supplies the probabilities needed to prepare the complement.

**Prerequisites.** [M04](#m04-a-reference-for-the-flag-ensemble), [M13](#m13-the-effective-channel-for-one-block).

**Conceptual connection.** Degradability supplies concavity of coherent information as a function of the channel input.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M15 The maximally mixed input

**Central question.** Why does the best coherent-information bound use the maximally mixed input?

**Understanding target.** Track Pauli conjugation through the phase mixture. Combine invariance under this symmetry with concavity to bound every input by its Pauli average.

**Prerequisites.** [M14](#m14-degrading-to-the-environment).

**Conceptual connection.** Blockwise flag processing may depend on the entire error string. The input Pauli symmetry still holds.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf).

### M16 Bell labels and residual uncertainty

**Central question.** What quantity remains after evaluating coherent information at the maximally mixed input?

**Understanding target.** Use the orthogonal maximally entangled states indexed by phase-error strings to obtain $`n-H(X^n\mid YQ)`$.

**Prerequisites.** [M07](#m07-information-in-classical-and-quantum-registers), [M15](#m15-the-maximally-mixed-input).

**Conceptual connection.** The channel converse becomes a bound on the available information about a classical error string.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf).

### M17 A one-site instrument from a joint processor

**Central question.** Why can the arbitrary block instrument be analyzed one site at a time?

**Understanding target.** Expand the information by the chain rule, fix past error labels and average future flags. Identify the map that acts on the current site under these conditions.

**Prerequisites.** [M03](#m03-independent-errors-across-a-block), [M07](#m07-information-in-classical-and-quantum-registers), [M16](#m16-bell-labels-and-residual-uncertainty).

**Conceptual connection.** The fixed past labels enter a proof decomposition. The physical early processor receives only the flags.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M18 A canonical branch for each effect

**Central question.** How does the positive square-root instrument bound other ways of handling the same outcome?

**Understanding target.** Factor the Kraus operators through $`\sqrt{E_y}`$ on its support. Use data processing to compare residual quantum information for branches with the same effect.

**Prerequisites.** [M05](#m05-a-measurement-with-residual-state), [M07](#m07-information-in-classical-and-quantum-registers), [M17](#m17-a-one-site-instrument-from-a-joint-processor).

**Conceptual connection.** This bounds the arbitrary quantum register by the entropy of a conditional qubit reference state.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M19 The entropy envelope in Bloch coordinates

**Central question.** How much uncertainty remains in the error label for a fixed reference spectrum and transverse coordinate?

**Understanding target.** Use $`|z|\leq\sqrt{r^2-x^2}`$ to bound the binary diagonal entropy by the planar envelope. Identify the states that saturate the inequality.

**Prerequisites.** [M04](#m04-a-reference-for-the-flag-ensemble), [M06](#m06-binary-entropy-from-a-qubit-radius), [M18](#m18-a-canonical-branch-for-each-effect).

**Conceptual connection.** The equality conditions identify the geometry of the receiver's optimal outcomes.

**Canonical sources.** [Converse](../science/converse.md).

### M20 A convex bound for averaged branches

**Central question.** What prevents a spread of branch entropies and transverse coordinates from beating the planar envelope?

**Understanding target.** Explain how joint convexity permits averaging across outcomes, sites and prior histories. Identify where entropy monotonicity permits replacing the reference entropy average by the quantum information actually retained.

**Prerequisites.** [M08](#m08-a-dimension-bound-at-the-memory-cut), [M17](#m17-a-one-site-instrument-from-a-joint-processor), [M18](#m18-a-canonical-branch-for-each-effect), [M19](#m19-the-entropy-envelope-in-bloch-coordinates).

**Conceptual connection.** The bound depends on the mean transverse coordinate, fixed by the source, and one storage constraint.

**Canonical sources.** [Converse](../science/converse.md) · [Watrous §1.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf).

### M21 The complete upper-bound curve

**Central question.** How does the entropy envelope give both a rising branch and a plateau?

**Understanding target.** Evaluate the bound at the largest admissible retained quantum information, limited by both $`q`$ and the flag ensemble entropy $`\chi`$. Explain why data processing gives the same plateau at larger budgets.

**Prerequisites.** [M16](#m16-bell-labels-and-residual-uncertainty), [M20](#m20-a-convex-bound-for-averaged-branches).

**Conceptual connection.** This is the limiting rate that every ideal receiver in the model must satisfy.

**Canonical sources.** [Capacity theorem](../science/capacity.md).

### M22 Two posterior reference states

**Central question.** Which two states make the entropy envelope tight at a chosen subthreshold budget?

**Understanding target.** Use transverse coordinate $`x_0`$, common radius $`r=f^{-1}(q)`$ and opposite vertical coordinates. Choose branch weights that recover the prior's mean vertical coordinate.

**Prerequisites.** [M04](#m04-a-reference-for-the-flag-ensemble), [M19](#m19-the-entropy-envelope-in-bloch-coordinates), [M21](#m21-the-complete-upper-bound-curve).

**Conceptual connection.** The construction can use biased error probabilities because the two branch weights implement the prior.

**Canonical sources.** [Achievability](../science/achievability.md).

### M23 From desired states to physical effects

**Central question.** How can the flag instrument produce those reference states?

**Understanding target.** Construct positive effects using the inverse of the flag-amplitude matrix. Confirm that their sum is the identity and compute the outcome-conditioned state with a positive square-root Kraus operator.

**Prerequisites.** [M05](#m05-a-measurement-with-residual-state), [M22](#m22-two-posterior-reference-states).

**Conceptual connection.** This implements the capacity optimizer with two possible measurement outcomes per site.

**Canonical sources.** [Achievability](../science/achievability.md) · [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M24 Aligning and compressing residual states

**Central question.** Why is the mean residual entropy also a storage rate?

**Understanding target.** Relate a residual state's spectrum to its conditional reference spectrum. Apply outcome-dependent rotations and describe the typical subspace that stores the rotated residuals.

**Prerequisites.** [M06](#m06-binary-entropy-from-a-qubit-radius), [M22](#m22-two-posterior-reference-states), [M23](#m23-from-desired-states-to-physical-effects).

**Conceptual connection.** After alignment the quantum source has the same average state at every site. Schumacher coding then applies to the product source.

**Canonical sources.** [Achievability](../science/achievability.md) · [Watrous §5.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M25 Meeting a hard memory budget

**Central question.** How can a protocol use typical-subspace compression under a strict dimension bound?

**Understanding target.** Distinguish the entropy rate from a finite-block dimension. Reserve a positive rate slack for compression at an interior target, then use continuity of the curve to approach the desired clipped rate.

**Prerequisites.** [M08](#m08-a-dimension-bound-at-the-memory-cut), [M11](#m11-a-rate-for-protecting-unknown-data), [M21](#m21-the-complete-upper-bound-curve), [M24](#m24-aligning-and-compressing-residual-states).

**Conceptual connection.** This connects a source-coding theorem with an asymptotic storage rate to the allowed dimension at every block size.

**Canonical sources.** [Achievability](../science/achievability.md) · [Watrous §5.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M26 The syndrome as a compression bin

**Central question.** How does the late syndrome make the residual flag record operational?

**Understanding target.** Explain the classical–quantum Slepian–Wolf decoder with $`Hx`$ as its bin index. Give the limiting number of independent checks per channel use and connect it to the logical rate.

**Prerequisites.** [M07](#m07-information-in-classical-and-quantum-registers), [M09](#m09-parity-checks-from-commuting-stabilizers), [M24](#m24-aligning-and-compressing-residual-states), [M25](#m25-meeting-a-hard-memory-budget).

**Conceptual connection.** One binary check per independent row costs one data-code dimension in logarithmic units.

**Canonical sources.** [Achievability](../science/achievability.md) · [Devetak and Winter](https://arxiv.org/abs/quant-ph/0209029).

### M27 Recovery of an arbitrary logical state

**Central question.** What does correct identification of the error string guarantee?

**Understanding target.** Apply the inferred phase operator to the encoded state. Bound the logical error by the probability of an incorrect label and the effect of imperfect flag compression.

**Prerequisites.** [M11](#m11-a-rate-for-protecting-unknown-data), [M25](#m25-meeting-a-hard-memory-budget), [M26](#m26-the-syndrome-as-a-compression-bin).

**Conceptual connection.** The same correction operates on payloads entangled with a reference. Correct-label events recover the full code state.

**Canonical sources.** [Achievability](../science/achievability.md) · [Watrous §3.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M28 Finite blocks and decoder resources

**Central question.** What must be counted when turning the asymptotic recipe into a finite receiver?

**Understanding target.** Track the actual held dimension, available rate slack, compression failure and syndrome-decoding error. Separate the two-outcome early operation from the computational and quantum resources required by a general late decoder.

**Prerequisites.** [M24](#m24-aligning-and-compressing-residual-states), [M25](#m25-meeting-a-hard-memory-budget), [M26](#m26-the-syndrome-as-a-compression-bin), [M27](#m27-recovery-of-an-arbitrary-logical-state).

**Conceptual connection.** These quantities determine how much of the capacity gain a concrete finite implementation can realize.

**Canonical sources.** [Finite-block resources](../science/finite-block.md).

### M29 Explaining the numerical gain

**Central question.** What does an interior point of the curve buy over mixing the two endpoint strategies?

**Understanding target.** For $`p=1/2`$, $`c=0.8`$ and $`q=0.20`$, compare the modeled rate of the weak receiver with immediate measurement and with endpoint time-sharing at the same memory budget.

**Prerequisites.** [M21](#m21-the-complete-upper-bound-curve), [M23](#m23-from-desired-states-to-physical-effects), [M27](#m27-recovery-of-an-arbitrary-logical-state).

**Conceptual connection.** The equal-budget comparison isolates the benefit of keeping some quantum information from each flag.

**Canonical sources.** [Capacity theorem](../science/capacity.md).

### M30 The memory–capacity statement

**Central question.** Which assumptions, mechanism and converse jointly establish the result?

**Understanding target.** State the independent phase-error and pure-flag model, the timing rule and the error criterion. Explain why the explicit protocol reaches an upper bound that allows joint early flag processing.

**Prerequisites.** [M12](#m12-two-routes-to-the-capacity), [M21](#m21-the-complete-upper-bound-curve), [M27](#m27-recovery-of-an-arbitrary-logical-state), [M28](#m28-finite-blocks-and-decoder-resources), [M29](#m29-explaining-the-numerical-gain).

**Conceptual connection.** The result characterizes asymptotic transmission under the specified memory budget. Finite implementations can be evaluated through their corresponding storage and decoding resources.

**Canonical sources.** [Capacity theorem](../science/capacity.md).
