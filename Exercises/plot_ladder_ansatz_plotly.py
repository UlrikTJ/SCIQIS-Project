import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from qcircsim import QuantumCircuit, expectation


def run_ansatz(qubits, layers, theta):
    qc = QuantumCircuit(qubits)
    for _ in range(layers):
        for q in range(qubits):
            qc.ry(theta, q)
        for q in range(qubits - 1):
            qc.cx(q, q + 1)
    return qc.statevector()


def pauli_expectation(state, operator='Z'):
    ez = expectation(state, operator * state.num_qubits)
    return ez


if __name__ == "__main__":
    n_qubits = [2, 3]
    n_layers = [1, 2, 3]
    thetas = np.linspace(0, 2 * np.pi, 200)

    # Compute expectation values
    ezs = [[[pauli_expectation(run_ansatz(nq, nl, th)) for th in thetas]
            for nl in n_layers]
           for nq in n_qubits]
    ezs = np.array(ezs)

    # Colors matching high-contrast professional palette
    colors = ['#0F4C81', '#E74C3C', '#00A86B']

    # Create subplots (2 rows, 1 column) sharing X axis
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=('<b>2 Qubits</b>', '<b>3 Qubits</b>')
    )

    # Add traces for 2 qubits (row 1) and 3 qubits (row 2)
    for i, nq in enumerate(n_qubits):
        pauli_label = 'Z' * nq
        for j, nl in enumerate(n_layers):
            layer_label = f'{nl} {"Layer" if nl == 1 else "Layers"}'
            
            fig.add_trace(
                go.Scatter(
                    x=thetas,
                    y=ezs[i, j],
                    mode='lines',
                    name=layer_label,
                    line=dict(color=colors[j], width=2.5),
                    legendgroup=layer_label,
                    showlegend=(i == 0),  # Only show legend once
                    hovertemplate=f'<b>{nq} Qubits ({nl}L)</b><br>θ: %{{x:.3f}} rad<br>⟨{pauli_label}⟩: %{{y:.4f}}<extra></extra>'
                ),
                row=i+1, col=1
            )

    # X-axis tick positions and unicode pi labels (rendered cleanly across all static & interactive Plotly engines)
    tick_vals = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    tick_text = ['0', 'π/2', 'π', '3π/2', '2π']

    # Update axis layouts and styling
    fig.update_xaxes(
        tickvals=tick_vals,
        ticktext=tick_text,
        range=[0, 2 * np.pi],
        showgrid=True,
        gridcolor='rgba(200, 200, 200, 0.4)',
        gridwidth=1,
        griddash='dash',
        mirror=True,
        ticks='inside',
        showline=True,
        linecolor='black'
    )
    
    fig.update_xaxes(title_text='<b>θ (radians)</b>', title_standoff=6, row=2, col=1)

    fig.update_yaxes(
        title_text='<b>Expectation Value ⟨ZZ⟩</b>',
        title_standoff=8,
        range=[-1.08, 1.08],
        showgrid=True,
        gridcolor='rgba(200, 200, 200, 0.4)',
        gridwidth=1,
        griddash='dash',
        mirror=True,
        ticks='inside',
        showline=True,
        linecolor='black',
        row=1, col=1
    )

    fig.update_yaxes(
        title_text='<b>Expectation Value ⟨ZZZ⟩</b>',
        title_standoff=8,
        range=[-1.08, 1.08],
        showgrid=True,
        gridcolor='rgba(200, 200, 200, 0.4)',
        gridwidth=1,
        griddash='dash',
        mirror=True,
        ticks='inside',
        showline=True,
        linecolor='black',
        row=2, col=1
    )

    # Position subplot titles cleanly above each subplot box
    for annotation in fig['layout']['annotations']:
        annotation['font'] = dict(size=12, family='Arial', color='black')

    # Layout styling
    fig.update_layout(
        title=dict(
            text='<b>Ladder Ansatz Circuit</b>',
            x=0.5,
            y=0.98,
            xanchor='center',
            font=dict(size=16, family='Arial')
        ),
        template='plotly_white',
        width=850,
        height=580,
        margin=dict(l=85, r=130, t=65, b=50),
        legend=dict(
            title=dict(text='<b>Circuit Layers</b>'),
            x=1.02,
            y=0.5,
            xanchor='left',
            yanchor='middle',
            bgcolor='rgba(250, 250, 250, 0.9)',
            bordercolor='rgba(200, 200, 200, 0.8)',
            borderwidth=1
        )
    )

    # Save as HTML with MathJax enabled for interactive viewing and static PNG image
    fig.write_html('ladder_ansatz_interactive.html', include_mathjax='cdn')
    fig.write_image('ladder_ansatz_plotly.png', scale=2)
    print("Saved Plotly figure to ladder_ansatz_interactive.html and ladder_ansatz_plotly.png")
