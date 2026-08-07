import numpy as np
import matplotlib.pyplot as plt
from qcircsim import QuantumCircuit, expectation


def run_ansatz(qubits, layers, theta, print_circuit=False):
    qc = QuantumCircuit(qubits)
    for _ in range(layers):
        for q in range(qubits):
            qc.ry(theta, q)
        for q in range(qubits-1):
            qc.cx(q, q+1)

    if print_circuit:
        print(qc)

    return qc.statevector()

def pauli_expectation(state, operator='Z'):
    ez = expectation(state, operator * state.num_qubits)
    return ez


if __name__ == "__main__":
    n_qubits = [2, 3]
    n_layers = [1, 2, 3]
    thetas = np.linspace(0, 2*np.pi, 180, endpoint=False)

    ezs = [[[pauli_expectation(run_ansatz(nq, nl, th))
            for th in thetas]
            for nl in n_layers]
            for nq in n_qubits]
    ezs = np.array(ezs)

    np.save('ladder_ansatz_data.npy', ezs)

    for i,nq in enumerate(n_qubits):
        for j,nl in enumerate(n_layers):
            print(f'\nLadder ansatz circuit with {nq} qubits and {nl} layers:\n')
            run_ansatz(nq, nl, 0, True)  # purely to visualize circuits
            plt.plot(thetas, ezs[i,j], label=f'{nq} qubits, {nl} layers')
            plt.legend()
    plt.title('ladder ansatz circuit')
    plt.xlabel('$\\theta$')
    plt.ylabel('<Z..Z>')
    plt.savefig('ladder_ansatz.png', )