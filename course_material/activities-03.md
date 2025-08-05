# SCIQIS activities 03

## More NumPy practice

1. Read this tutorial on the powerful but confusing `einsum` function while testing it on the side: [Einsum Visualized. A Swiss army knife of the array… | by Lev Maximov | Better Programming](https://betterprogramming.pub/einsum-visualized-c050903145ef)
2. Read [this tutorial on RealPython](https://realpython.com/numpy-random-number-generator/) about random number generation and randomisation or, if you prefer, the [NumPy documentation about its random generator](https://numpy.org/doc/stable/reference/random/generator.html). Note that there was a large overhaul of the `np.random` module with version 1.17 (in 2019) as documented [here](https://numpy.org/doc/stable/reference/random/new-or-different.html), so quite a bit of the tutorials you find online may be using the deprecated version. Play around a bit as you go along.

## Random circuit sampling

You should now try to sample random quantum circuits. Experimentally sampling random circuits has been used e.g. by [Google](https://www.nature.com/articles/s41586-019-1666-5), [USTC](https://www.science.org/doi/full/10.1126/science.abe8770) and [Xanadu](https://www.nature.com/articles/s41586-022-04725-x) to demonstrate quantum computational advantage (or supremacy). Read/skim the first few pages of [Mullane - Sampling random quantum circuits: a pedestrian's guide](https://arxiv.org/abs/2007.07872) for a rough idea of what random circuit sampling entails and why it is interesting.

Here, you are not going to perform quantum experiments or to do classical simulation at the cutting edge, but simply use your quantum circuit simulator to generate more or less random circuits from fixed gates (H, X, Y, Z, CNOT, etc.) and/or parametrised gates (RX(θ), RY(θ), RZ(θ), CR(θ), etc.).

[Sim et al.](https://onlinelibrary.wiley.com/doi/abs/10.1002/qute.201900070) defines the _expressibility_ of a quantum circuit by comparing fidelities between pairs of output states of randomly sampled circuits. Specifically, they define it (in eq. 17) as the [Kullback-Leibler divergence](https://wikipedia.org/en/Kullback%E2%80%93Leibler_divergence#Definition) of the discrete distribution $P(F) = \hat P_\text{PQC}(F;\theta)$ with the discrete distribution $Q(F) = P_\text{Haar}(F) = (N-1)(1-F)^{(N-2)}$. The idea of expressibility is to quantify how close to a truly random circuit you can get. Lower values are better.

Here, $N$ is the dimensionality of the circuit, i.e. $N=2^n$ for $n$ qubits. 

$Q(F)$ is the theoretical distribution of fidelities when the unitary $U$ of the circuit is sampled uniformly from the distribution of all $n$-qubit unitaries (Haar-distributed). Note that for $n=1$, it is constant, $Q(F)=1$. The reason why it is not 1 but more like 0.013 in Figure 1c is because they plot the probabilities of ~75 discretised bins.

$P(F)$ is the distribution of fidelities $F = |\langle\psi_\Theta| \psi_\Phi\rangle|^2$ between pairs of states sampled from the output of the random circuit - here, specifically for parametrised circuits where $\Theta$ and $\Phi$ represent the set of randomly sampled gate parameters. $P(F)$ is continuous, but in a numerical experiment it will be discretised by building a histogram of the sampled fidelities.



1. Read sections 3.1.1 and 3.1.2 of Sim et al. and study Figure 1. This should give you a good idea of the main concept.
2. Using your circuit simulator, set up some code for generating random circuits. You can sample parameters of a fixed configuration of parametrised gates, as in Sim et al., and you can optionally also sample from a set of fixed gates, as described at the top of p.5 of Mullane.
3. Now create some code for calculating the expressibility of the circuit, i.e. sampling many circuits, calculating pairwise fidelities, and calculating the KL distance of a suitably discretised distribution of those fidelities with $Q(F)$. 
4. Can you recreate the results in Figure 1c of Sim et al.? Note that the phase of each $R(\phi)$ gate should be sampled uniformly in $[0;2\pi[$.
5. How about Figure 3? (Only a few points)
