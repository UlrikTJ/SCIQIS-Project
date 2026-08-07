import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from qcircsim import QuantumCircuit, expectation

# ---------------------------------------------------------
# Quantum Circuit Simulation
# ---------------------------------------------------------
def run_ansatz(qubits, layers, theta):
    qc = QuantumCircuit(qubits)
    for _ in range(layers):
        for q in range(qubits):
            qc.ry(theta, q)
        for q in range(qubits - 1):
            qc.cx(q, q + 1)
    return qc.statevector()

def pauli_expectation(state):
    return expectation(state, 'Z' * state.num_qubits)

# ---------------------------------------------------------
# Data Generation
# ---------------------------------------------------------
if __name__ == "__main__":
    n_qubits_list = [2, 3]
    n_layers_list = [1, 2, 3]
    thetas = np.linspace(0, 2 * np.pi, 400)

    ezs = np.zeros((len(n_qubits_list), len(n_layers_list), len(thetas)))
    for i, nq in enumerate(n_qubits_list):
        for j, nl in enumerate(n_layers_list):
            ezs[i, j] = [pauli_expectation(run_ansatz(nq, nl, th)) for th in thetas]

    np.save('ladder_ansatz_data.npy', ezs)

    # ---------------------------------------------------------
    # Publication Quality Configuration (Nature / IEEE Standard)
    # ---------------------------------------------------------
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman', 'serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9,
        'axes.labelsize': 10,
        'axes.titlesize': 10,
        'xtick.labelsize': 8.5,
        'ytick.labelsize': 8.5,
        'legend.fontsize': 8,
        'figure.titlesize': 11,
        'pdf.fonttype': 42,
        'ps.fonttype': 42
    })

    # High-contrast colorblind-safe Okabe-Ito / Colorbrewer Palette
    # Layer 1: Solid Dark Blue, Layer 2: Vermilion Red (Dashed), Layer 3: Slate Grey (Dotted)
    colors = ['#114B7A', '#C0392B', '#27AE60']
    linestyles = ['-', '--', '-.']

    fig, axes = plt.subplots(2, 1, figsize=(6.5, 4.5), sharex=True, dpi=300)

    for i, nq in enumerate(n_qubits_list):
        ax = axes[i]
        
        # Reference Zero line
        ax.axhline(0, color='#BDC3C7', linestyle=':', linewidth=0.8, alpha=0.7)

        for j, nl in enumerate(n_layers_list):
            label = f'{nl} {"layer" if nl == 1 else "layers"}'
            ax.plot(thetas, ezs[i, j], label=label, color=colors[j],
                    linestyle=linestyles[j], linewidth=1.4)

        # Non-colliding Panel Header (Top-Left inside, moved slightly right/up or as axis title)
        panel_letter = '(a)' if i == 0 else '(b)'
        ax.set_title(f'{panel_letter} $N = {nq}$ Qubits', loc='left', fontsize=9.5, fontweight='bold', pad=4)

        ax.set_ylabel(r'$\langle Z^{\otimes N} \rangle$', fontsize=9.5)
        ax.set_ylim(-1.12, 1.12)
        ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
        
        # Subtle grid ticks
        ax.grid(True, linestyle=':', alpha=0.35, color='#BDC3C7')
        ax.tick_params(direction='in', top=True, right=True, length=3.5, width=0.6)
        
        for spine in ax.spines.values():
            spine.set_linewidth(0.8)

    # Shared X-axis configuration
    axes[1].set_xlabel(r'Variational Parameter $\theta$ (rad)', fontsize=9.5)
    axes[1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    axes[1].set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    axes[1].set_xlim(0, 2*np.pi)

    # Clean, non-overlapping Legend placed tightly outside on the right
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, title='Circuit Layers', bbox_to_anchor=(1.01, 0.5), loc='center left',
               frameon=True, framealpha=1.0, edgecolor='#BDC3C7', facecolor='#FFFFFF', fontsize=8)

    # Figure Title
    fig.suptitle('Expectation Value $\\langle Z^{\\otimes N} \\rangle$ of the Ladder Ansatz Circuit',
                 fontsize=10.5, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.subplots_adjust(top=0.90, right=0.84, hspace=0.25)
    
    # Save vectorized PDF and high-res PNG
    plt.savefig('ladder_ansatz_publication.png', dpi=300, bbox_inches='tight')
    plt.savefig('ladder_ansatz_publication.pdf', bbox_inches='tight')
