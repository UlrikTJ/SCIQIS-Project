import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
from qcircsim import QuantumCircuit, expectation

# ---------------------------------------------------------
# Quantum Circuit Simulation Logic
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
    thetas = np.linspace(0, 2 * np.pi, 300)

    # Calculate expectation values
    ezs = np.zeros((len(n_qubits_list), len(n_layers_list), len(thetas)))
    for i, nq in enumerate(n_qubits_list):
        for j, nl in enumerate(n_layers_list):
            ezs[i, j] = [pauli_expectation(run_ansatz(nq, nl, th)) for th in thetas]

    # Save array
    np.save('ladder_ansatz_data.npy', ezs)

    # ---------------------------------------------------------
    # Custom Modern Theme & Layout Setup
    # ---------------------------------------------------------
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
    
    # Palette: Premium Deep Neon (Cyan, Coral, Violet)
    colors = ['#00D2FF', '#FF5376', '#9B51E0']
    bg_color = '#0F172A'      # Slate 900
    card_bg = '#1E293B'       # Slate 800
    text_color = '#F8FAFC'    # Slate 50
    muted_text = '#94A3B8'    # Slate 400
    grid_color = '#334155'    # Slate 700

    fig = plt.figure(figsize=(12, 7.5), facecolor=bg_color, dpi=200)
    gs = gridspec.GridSpec(2, 2, width_ratios=[3.2, 1], height_ratios=[1, 1], wspace=0.15, hspace=0.28)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    ax_info = fig.add_subplot(gs[:, 1])

    axes = [ax1, ax2]

    # ---------------------------------------------------------
    # Main Line Subplots
    # ---------------------------------------------------------
    for i, nq in enumerate(n_qubits_list):
        ax = axes[i]
        ax.set_facecolor(card_bg)
        
        # Zero baseline highlight
        ax.axhline(0, color='#475569', linestyle=':', linewidth=1.2, zorder=1)

        for j, nl in enumerate(n_layers_list):
            y_vals = ezs[i, j]
            label = f'{nl} {"Layer" if nl == 1 else "Layers"}'
            
            # Glow effect layer
            ax.plot(thetas, y_vals, color=colors[j], linewidth=4.0, alpha=0.25, zorder=2)
            # Core line
            ax.plot(thetas, y_vals, label=label, color=colors[j], linewidth=2.2, zorder=3)

            # Find and mark minimum energy / expectation points
            min_idx = np.argmin(y_vals)
            ax.scatter(thetas[min_idx], y_vals[min_idx], color=colors[j], s=35, zorder=4, edgecolors=text_color, linewidth=1.2)

        # Axis Styling
        ax.set_ylim(-1.12, 1.12)
        ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
        ax.set_yticklabels(['-1.0', '-0.5', '0.0', '0.5', '1.0'], color=text_color, fontsize=10)
        ax.tick_params(colors=muted_text, width=1)
        ax.grid(True, linestyle='--', alpha=0.4, color=grid_color)
        
        # Card Badge Title
        ax.text(0.02, 0.90, f' {nq} QUBITS ', transform=ax.transAxes,
                fontsize=10, fontweight='bold', color=text_color,
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#334155', edgecolor='none', alpha=0.9))

        ax.set_ylabel(r'$\langle Z^{\otimes N} \rangle$', fontsize=11, color=text_color, labelpad=8)
        
        # Hide spines
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_color(grid_color)
            ax.spines[spine].set_linewidth(1.2)

    # Bottom X-Axis
    ax2.set_xlabel(r'Rotation Angle $\theta$', fontsize=12, color=text_color, labelpad=8)
    ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax2.set_xticklabels(['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], color=text_color, fontsize=11)
    ax2.set_xlim(0, 2*np.pi)
    plt.setp(ax1.get_xticklabels(), visible=False)

    # ---------------------------------------------------------
    # Right Sidebar Dashboard Card
    # ---------------------------------------------------------
    ax_info.set_facecolor(card_bg)
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    ax_info.axis('off')
    
    # Border for info card
    for spine in ax_info.spines.values():
        spine.set_color(grid_color)

    # Custom Legend inside Info Card
    ax_info.text(0.08, 0.90, 'CIRCUIT CONFIG', fontsize=11, fontweight='bold', color=muted_text, va='center')
    
    for j, nl in enumerate(n_layers_list):
        y_pos = 0.78 - j * 0.10
        # Glowing line indicator
        ax_info.plot([0.08, 0.22], [y_pos, y_pos], color=colors[j], linewidth=4)
        ax_info.plot([0.08, 0.22], [y_pos, y_pos], color=colors[j], linewidth=8, alpha=0.3)
        ax_info.text(0.28, y_pos, f'{nl} {"Layer" if nl == 1 else "Layers"} Ansatz', color=text_color, fontsize=10.5, fontweight='bold', va='center')

    # Metrics Summary Box
    ax_info.text(0.08, 0.44, 'ANALYTICS SUMMARY', fontsize=11, fontweight='bold', color=muted_text, va='center')
    
    stats_text = (
        r"• Parameter: $\theta \in [0, 2\pi)$" + "\n" +
        r"• Observable: Pauli $Z^{\otimes N}$" + "\n" +
        "• Minimum: -1.000 (Ground)" + "\n" +
        "• Maximum: +1.000 (Excited)" + "\n" +
        "• Entanglement: CX Ladder"
    )
    ax_info.text(0.08, 0.38, stats_text, color=text_color, fontsize=9.5, linespacing=1.6, va='top')

    # Footer note inside card
    ax_info.text(0.08, 0.05, 'Simulated via QCircSim Engine', color=muted_text, fontsize=8.5, style='italic')

    # ---------------------------------------------------------
    # Global Dashboard Header
    # ---------------------------------------------------------
    fig.suptitle('QUANTUM LADDER ANSATZ EXPECTATION VALUES',
                 fontsize=14, fontweight='bold', color=text_color, x=0.08, y=0.97, ha='left')
    fig.text(0.08, 0.92, 'Variational Quantum Eigensolver (VQE) Pauli-Z Measurement Landscapes',
             fontsize=10, color=muted_text, ha='left')

    # Adjust layout & Save high-res poster
    plt.subplots_adjust(top=0.86, bottom=0.10, left=0.08, right=0.96)
    plt.savefig('ladder_ansatz_ultimate.png', dpi=300, facecolor=bg_color)
