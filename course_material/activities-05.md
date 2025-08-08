# SCIQIS activities 05

## QuTiP

1. Browse through the many tutorials on [QuTiP's website](https://qutip.org/qutip-tutorials/). If some of them are aligned with your quantum science interests, then feel free to dig into them and code along.

### Solving master equations with QuTiP

2. Starting from [this QuTiP tutorial](https://nbviewer.org/urls/qutip.org/qutip-tutorials/tutorials-v5/time-evolution/006_photon_birth_death.ipynb) which replicates [one of the papers on cavity QED](http://dx.doi.org/10.1038/nature05589) that contributed to the 2012 Nobel prize of Serge Haroche, try to come up with new ways to visualise the results. This could be as a static plot, an animation, or an interactive plot. 
3. Change the parameters of the simulation, like changing the initial state, the time steps, the number of trajectories, the coupling rate, environment temperate, etc. - you may discover something interesting by varying these.

Note that you can store all trajectories with the `keep_runs_results` option to `mcsolve` described [here](https://qutip.readthedocs.io/en/stable/guide/dynamics/dynamics-monte.html) (under Monte Carlo Solver Result), and then access e.g. the expectation of the operators in `e_ops` at each time with the result's `runs_expect` property.

## Calculating density matrices

