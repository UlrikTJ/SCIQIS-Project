# SCIQIS activites 04

## Matplotlib and pretty plots

Visualising data is a core skill of any scientist. It enables you to explore and understand your data and calculations, and to tell a story about the data to your audience. Apart from static plots, it can also be very useful to use animations or interactive plots to present and explore your data.

Making beautiful AND informative plots or other visualisations is an art form that is very much worth investing some time into practicing. For communication of scientific results, your number one priority should be on conveying a clear and unambigous message that the recipient can understand with as little mental effort as possible. However, this often goes hand-in-hand with making the graphical style look pretty. 

There are a bunch of very nice plotting libraries for Python, also many that do high-quality interactive visualisations. Prominent examples are [Plotly](https://plotly.com/python/), [Bokeh](https://bokeh.org), [Vega-Altair](https://altair-viz.github.io) and [seaborn](https://seaborn.pydata.org). It is fun to play around with these libraries and get inspiration for how to present data in clever, enlightening ways.

Good old [Matplotlib](https://matplotlib.org) is however still the "industry standard" and go-to plotting tool for most scientists working in Python.

1. I included an assorted list of high-quality guides and tutorials in the matplotlib section of [references.md](./references.md). Skim these, just so you know what's in them, for future reference.
2. Practice your Matplotlib plot manipulation and graphic skills by making 2 different prettified versions of the simple plot of some artificial data in the [Matplotlib exercise](../exercises/Matplotlib%20exercise.ipynb) notebook.
3. When you are happy with one or both of your plots, export them as an image and share them on the [#matplotlib-exercise](https://discord.com/channels/1397692599908700241/1402929169481863310) Discord channel.
4. Next, try using [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) (most easily with [interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)) and/or [animation](https://matplotlib.org/stable/users/explain/animations/animations.html) to make the plot come alive.\
The demos I showed in class are in the [Visualisation](../tutorials/Visualisation.ipynb) notebook.

## Gaussian states and gates (operations)

In quantum optics, an important class of quantum states are those with Gaussian wavefunctions over the $x$-quadrature/position/amplitude variable. These include coherent states (which, approximately, is what comes out of a laser), thermal states (like a lightbulb), vacuum states (no photons - but still some noise due to Heisenberg), and squeezed states (non-classical states with many applications in QIP).

Jonatan from QPIT wrote a very handy 10-page overview of the most important concepts, states and operations: [Gaussian states and operations – a quick reference](https://arxiv.org/abs/2102.05748). You won't have time to read it all now, but you can find most of the formulas you need for this exercise in there. For a more authoritative and in-depth review of the field, [Weedbrook et al.](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.84.621) is the go-to reference. 

This exercise has three objectives. You should

- learn about Gaussian states and their representation in phase space,
- try out interactive plots using `ipywidgets` and/or animated plots using Matplotlib's `animation` module,  
- practice writing a computational narrative in the form of a notebook with text, code, and static + interactive/animated plots.

1. Understand as a minimum equations (20) and (22) in Jonatan's reference, as well as those in gray boxes in section III. The covariance matrices and displacement vectors of the four classes of single-mode Gaussian states mentioned above are presented in section VI. We will not consider two-mode or multi-mode states in this exercise.
2. Create functions for calculating the Wigner function of a general Gaussian state.
3. Using contour plot, 3D surface plot, or similar, plot the Wigner functions of various single-mode Gaussian states based on the formulas indicated above.\
Don't spend too much time on optimising the visuals of the plots in this exercise - you can go with the defaults, if you wish. But decide on a fixed visual style that you will maintain for all your plots.
4. Now, try out `interact` and/or `FuncAnimation` for varying parameters of your state plots (for example the coherent state amplitude or the degree of squeezing).
5. Write functions for performing Gaussian operations on your Gaussian states: displacement, phase shift and squeezing.
6. Your overall task is now to write a notebook, introducing Gaussian states and operations to your fellow students in a narrative style with text mixed with code and visualisations. The focus here should be on the physics and the visual explanation of it, not so much on discussing the code.
7. At the end of the day, share your notebook – however incomplete – on Discord. 

