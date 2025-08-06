# SCIQIS activities 02

## NumPy basics and not-so-basics

1. Work your way through the `Numpy arrays.ipynb` notebook in the tutorials folder. In places where I didn't explicitly write what I wanted to show (because it was initially intended to be shown in class), try to think about what I intended to illustrate.
2. Unless you are quite experienced with NumPy, work through this  great illustrated tutorial, testing the more challenging concepts as you go along: [NumPy Illustrated: The Visual Guide to NumPy (Lev Maximov)](https://betterprogramming.pub/3b1d4976de1d?sk=57b908a77aa44075a49293fa1631dd9b).
3. If/when you feel like it, try to do some of the [100 numpy exercises (with solutions)](https://github.com/rougier/numpy-100). Beware - they quickly get challenging! Be sure to think/try for a while before referring to the answer or hint that can be revealed by executing `hint(n)` or `answer(n)`.\
You can run them in as local environment by cloning or downloading the repository and then doing
    ```
    $ uv init
    $ uv add -r requirements.txt
    $ uv add ipykernel
    $ uv run ipykernel install --user --name 'numpy-100'
    $ uv run --with jupyter jupyter lab
    ```

## A simple quantum circuit simulator

There are probably a hundred or more quantum computing simulators out there, but let's add to that count! :) Your first quantum information related exercise will be to simulate quantum circuits like this one (which you will recognise as the quantum teleportation circuit):

![Quantum teleportation circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Quantum_teleportation_circuit.svg/1920px-Quantum_teleportation_circuit.svg.png)

1. For familiarizing or refreshing yourself on qubits, quantum gates and quantum circuits, take a moment to skim chapters 2, 3, 4.1, 4.2, 5.3 and 7.1 of [Scott Aaronson's lecture notes](https://www.scottaaronson.com/qclec.pdf) - or go to Jonas for a quick intro.
   For a more rigorous treatment, see [these lessons by John Watrous](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information).
   Somewhere in-between is the [Wikipedia page on quantum gates](https://wikipedia.org/en/Quantum_logic_gate).
   Wikipedia's [List of quantum logic gates](https://wikipedia.org/en/List_of_quantum_logic_gates) is a concise list of common gates.
2. Set up a new public repository on your Github account, to be used for this exercise. While developing, remember to practice a git workflow: commit at appropriate times (remember meaningful commit messages), sync (pull-push), use branches if needed (or just for practice).
3. I suggest you to start exploring your code in a Jupyter notebook. Then, as you create more-or-less complete pieces of code, you can move this to a separate .py file that you import into the notebook. You can also stay entirely in the notebook interface or completely avoid it, if you prefer.
4. Now, using Numpy arrays and functions, play around for a while with arrays representing qubits and gates, and convince yourself that they do what you expect. For example, test these:
    - $X$, $Y$, $Z$, $H$ and $T$ gates applied to states $|0\rangle$, $|+\rangle$, $|1\rangle$, $|T\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt{2}$, etc.
    - $CNOT$ and $CZ$ gates applied to states $|00\rangle$, $|+0\rangle$, $|++\rangle$, etc.
5. When you're convinced that you understand the fundamental way to represent qubits and gates as vectors and matrices, go to the main task: Build a quantum circuit simulator that can take an input state vector $|\psi_{{in}}\rangle$ and a series of gates $\{U_i\}$ and use this to calculate the output state vector $|\psi_{out}\rangle = U_n\ldots U_1 |\psi_{in}\rangle$. 
   Below are some hints and suggestions for different directions you could take:
    - Before even starting writing reusable code, play around for a while with arrays representing qubits and gates, and convince yourself that they do what you expect.
	- You can make this as simple or as complex as you feel comfortable with, but it's a good idea to start simple, test that it works, and then expand the scope gradually.
	- A single-qubit simulator is significantly simpler than a simulator for multiple qubits. You may wish to start with just one qubit.
	- For multi-qubit circuits, you need the tensor product between the Hilbert spaces to get e.g. $|\psi\rangle_A \otimes |\phi\rangle_B$ and $U_A \otimes U_B$. The matrix of the tensor product is called the [Kronecker product](https://omni.wikiwand.com/en/articles/Kronecker_product) and is implemented in NumPy by `np.kron`.
	- No need to implement all possible gates. Just choose a representative set - it can easily be expanded later on.
	- You can implement a measurement at the end: Given an $n$-qubit output state $|\psi_{out}\rangle$, the probability of measuring the bit string $x_1\ldots x_n$ is $|\langle x_1\ldots x_n|\psi_{out}\rangle|^2$. One way of sampling from this probability distribution is using `rng = np.random.default_rng(); rng.choice(...)`.
    - Instead of just a single input state, your function could take an array of input states to simulate multiple initial states in one go. This could e.g. be used to calculate the performance of the teleportation circuit for a range of possible input states.
	- If you're comfortable with object-oriented programming or wish to practice it, you could create classes representing e.g. states, gates, and circuits.
6. A useful test of your circuit simulator is whether it correctly calculates the output of the [Quantum Fourier Transform](https://en.wikipedia.org/wiki/Quantum_Fourier_transform). Try to test it for three qubits. That circuit and its output are presented in the [Example](https://en.wikipedia.org/wiki/Quantum_Fourier_transform#Example) section.
    - For example, taking the input $|000\rangle$ should result in the output state $\frac{1}{\sqrt{8}} \sum_{k=0}^7 |k\rangle = |000\rangle + |001\rangle + \ldots + |111\rangle$.
    - The input state $|011\rangle$ should result in the state $\frac{1}{\sqrt{8}} \sum_{k=0}^7 \omega^{3k}|k\rangle$.
    - Both of the states above should give equal probabilities for measuring all the 8 possible measurement results. For input states in superposition of the computational basis states, this is no longer the case. For example, the input state $\frac{1}{\sqrt{2}}(|000\rangle + |011\rangle)$ should give the output $\frac{1}{4} \sum_{k=0}^7 (1 + \omega^{3k})|k\rangle$. The probabilities of getting 0 (=`000`) or 4 (=`100`) in the measurement are 1/4 each, while the other outcomes are non-zero but smaller.