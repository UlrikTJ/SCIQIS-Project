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

    # Create figure with 2 subplots stacked vertically sharing the X axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True, dpi=150)
    axes = [ax1, ax2]

    # High-contrast professional palette (Deep Navy Blue, Bright Crimson/Red, Emerald Teal)
    colors = ['#0F4C81', '#E74C3C', '#00A86B']

    for i, nq in enumerate(n_qubits):
        ax = axes[i]
        for j, nl in enumerate(n_layers):
            print(f'\nLadder ansatz circuit with {nq} qubits and {nl} layers:\n')
            run_ansatz(nq, nl, 0, True)  # purely to visualize circuits
            label = f'{nl} {"Layer" if nl == 1 else "Layers"}'
            ax.plot(thetas, ezs[i, j], label=label, linewidth=2.0, color=colors[j])

        # Direct line labels placed along right side (theta ~ 5.2 - 5.8 rad)
        # Gradient is computed ONLY from the exact curve span under the textbox size (~0.4 rad theta width)
        text_span_theta = 0.40  # Theta width matching the physical size of the text box

        for j, nl in enumerate(n_layers):
            if j == 0:  # 1 layer
                th_pos = 5.25
            elif j == 1:  # 2 layers
                th_pos = 5.50
            else:  # 3 layers
                th_pos = 5.75

            # Select data points strictly within the textbox footprint [th_pos - half_span, th_pos + half_span]
            box_mask = (thetas >= (th_pos - text_span_theta / 2.0)) & (thetas <= (th_pos + text_span_theta / 2.0))
            thetas_box = thetas[box_mask]
            ez_box = ezs[i, j, box_mask]

            # Fit 1st-degree linear slope directly over the curve section underlying the textbox
            poly = np.polyfit(thetas_box, ez_box, deg=1)
            dy_dth = poly[0]  # Exact line slope across the text box footprint
            
            # Sample exact data y-value at center position
            idx_pos = np.argmin(np.abs(thetas - th_pos))
            y_data = ezs[i, j, idx_pos]

            # Convert exact textbox footprint slope to display screen coordinates for true visual rotation angle
            p0 = ax.transData.transform((th_pos, y_data))
            p1 = ax.transData.transform((th_pos + 0.05, y_data + 0.05 * dy_dth))
            angle = np.degrees(np.arctan2(p1[1] - p0[1], p1[0] - p0[0]))

            lbl_text = f'{nl} {"layer" if nl == 1 else "layers"}'

            # Render styled text box aligned parallel with the curve section under the text box
            ax.annotate(
                lbl_text,
                xy=(th_pos, y_data),
                xytext=(0, 6),
                textcoords='offset points',
                color=colors[j],
                fontsize=8.5,
                fontweight='bold',
                ha='center',
                va='bottom',
                rotation=angle,
                rotation_mode='anchor',
                bbox=dict(
                    boxstyle='round,pad=0.25',
                    facecolor='#FFFFFF',
                    edgecolor=colors[j],
                    linewidth=1.0,
                    alpha=0.95
                )
            )

        ax.set_title(f'{nq} Qubits', fontsize=11, fontweight='bold', loc='left', pad=6)
        
        # Set y-axis label to specific Pauli tensor product: <ZZ> for 2 qubits, <ZZZ> for 3 qubits
        pauli_str = 'Z' * nq
        ax.set_ylabel(f'Expectation Value $\\langle {pauli_str} \\rangle$', fontsize=10)
        
        ax.grid(True, linestyle='--', alpha=0.4, color='#888888')
        ax.set_ylim(-1.08, 1.08)
        ax.tick_params(direction='in', top=True, right=True, labeltop=False)

    # Shared X-axis settings
    ax2.set_xlabel('$\\theta$ (rad)', fontsize=11)
    plt.xticks(
        [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
        ['$0$', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']
    )
    plt.xlim(0, 2*np.pi)

    fig.suptitle('Ladder Ansatz Circuit', fontsize=14, fontweight='bold', y=0.96)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.15)
    plt.savefig('ladder_ansatz_subplots.png', bbox_inches='tight')
