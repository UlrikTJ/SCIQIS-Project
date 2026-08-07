import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, Wedge
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
    
    # Grid for Polar Rose / Radar Surface Map (theta angle x layers radius)
    r_theta = np.linspace(0, 2 * np.pi, 360)
    
    # ---------------------------------------------------------
    # Creative Layout: Polar Quantum Wave Orbits & Phase Space
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(14, 8), facecolor='#05070F', dpi=200)
    
    # Custom Colormaps for 2 Qubits (Cyan/Electric) and 3 Qubits (Magenta/Neon Gold)
    cmap_2q = LinearSegmentedColormap.from_list('cyan_pulse', ['#00F2FE', '#4FACFE', '#000000'])
    
    # 2 Polar Subplots side-by-side representing Quantum Phase Ring Energy Maps
    ax1 = fig.add_subplot(121, projection='polar', facecolor='#0B0F19')
    ax2 = fig.add_subplot(122, projection='polar', facecolor='#0B0F19')

    axes = [ax1, ax2]
    titles = ['2-QUBIT LADDER ANSATZ PHASOR WAVE', '3-QUBIT LADDER ANSATZ PHASOR WAVE']
    glow_colors = [['#00F2FE', '#38EF7D', '#FF007F'], ['#FF007F', '#FFD200', '#7F00FF']]

    for i, nq in enumerate(n_qubits_list):
        ax = axes[i]
        
        # Grid aesthetics
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.grid(True, color='#1E293B', linestyle=':', linewidth=1.2)
        ax.tick_params(colors='#64748B', labelsize=9)
        
        # Custom Angular Ticks (Theta in multiples of pi)
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))
        ax.set_xticklabels(['$0$', '$\\pi/4$', '$\\pi/2$', '$3\\pi/4$', '$\\pi$', '$5\\pi/4$', '$3\\pi/2$', '$7\\pi/4$'],
                           color='#94A3B8', fontsize=10)
        
        # Radial Limits & Ticks (mapped expectation values converted to positive radii)
        ax.set_ylim(0, 2.5)
        ax.set_yticks([0.5, 1.0, 1.5, 2.0])
        ax.set_yticklabels(['', r'$\langle Z \rangle = -0.5$', r'$\langle Z \rangle = 0$', r'$\langle Z \rangle = +0.5$'],
                           color='#475569', fontsize=8)

        # Plot orbits for 1, 2, and 3 layers
        for j, nl in enumerate(n_layers_list):
            ezs = np.array([pauli_expectation(run_ansatz(nq, nl, th)) for th in r_theta])
            
            # Map expectation values [-1, 1] to radial distance r in [0.5, 2.5]
            radius = 1.5 + 0.8 * ezs
            
            color = glow_colors[i][j]
            
            # Outer aura glow
            ax.plot(r_theta, radius, color=color, linewidth=5.0, alpha=0.2)
            # Main Orbit Ribbon
            ax.plot(r_theta, radius, label=f'{nl} Layer{"s" if nl > 1 else ""}', color=color, linewidth=2.2)
            
            # Fill area between curve and zero-expectation ring (radius = 1.5)
            ax.fill_between(r_theta, 1.5, radius, color=color, alpha=0.08)

        # Center Quantum State Core Ring
        core_ring = Circle((0, 0), 0.5, transform=ax.transData._b, color='#00F2FE', alpha=0.1)
        ax.add_patch(core_ring)

        ax.set_title(titles[i], color='#F8FAFC', fontsize=11, fontweight='bold', pad=25)
        legend = ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.22), ncol=3,
                           frameon=True, facecolor='#0F172A', edgecolor='#334155', fontsize=9)
        for text in legend.get_texts():
            text.set_color('#E2E8F0')

    # ---------------------------------------------------------
    # Global Creative Title Banner & Cyberpunk Aesthetic
    # ---------------------------------------------------------
    fig.suptitle('QUANTUM ANSATZ POLAR ORBITAL DYNAMICS', fontsize=15, fontweight='bold', color='#F8FAFC', y=0.97)
    fig.text(0.5, 0.925, 'Pauli-Z Expectation Harmonics Mapped as Radial Quantum Wave Orbits',
             fontsize=10.5, color='#94A3B8', ha='center')

    # Creative Footer Note
    fig.text(0.5, 0.02, r'♦ Radial Distance $R(\theta) \propto \langle Z^{\otimes N} \rangle$  |  Center Core: Maximum Ground Interference  |  Outer Edge: Excited State',
             fontsize=8.5, color='#64748B', ha='center', style='italic')

    plt.subplots_adjust(top=0.82, bottom=0.18, wspace=0.35)
    plt.savefig('ladder_ansatz_creative.png', dpi=300, facecolor='#05070F')
