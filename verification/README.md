# Reproduce the numerical checks

From the repository root, run with Python 3 and NumPy installed.

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The script checks the two-outcome construction for 100 choices of prior, flag overlap, and memory. It samples 1,680 joint instruments on up to three flags, using a fixed random seed and including mixed residual states, and compares their coherent information with the memory bound. It also checks the finite compression dimension and binomial tail inequalities on 36 cases.

For uniform phase errors and overlap $`0.8`$, the computed rate at $`0.20`$ retained flag qubits per use is $`0.380322417`$. The immediate measurement and endpoint time-sharing rates are $`0.278071905`$ and $`0.359490021`$, respectively.

The [proof](../science/converse.md) establishes the converse for every instrument in the model. The sampled instruments check numerical identities and inequalities on the tested instances.
