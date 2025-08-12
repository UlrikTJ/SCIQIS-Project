# SCIQIS activities 07

## Gaussian state notebook peer feedback

In groups of 3, review each other's notebooks from the [activities-04](./activities-04.md) exercise on Gaussian states. I uploaded them on [#gaussian-states-notebook](https://discord.com/channels/1397692599908700241/1403002651574272140)

Spend ~10 minutes reading the notebook of each of the other group members. After reading both, take turns at giving **constructive** feedback to each other.

## Speeding up your code

Try to speed up your code for either quantum circuit simulation, Gaussian Wigner function calculation and/or density matrix ←→ Wigner function conversion.

Start by profiling it with e.g. %timeit, %prun and %lprun. Then, first try to refactor your code to make efficient use of NumPy's array handling. Next, see if you can make use of Numba, numexpr, `functools.lru_cache`, or maybe Jax or parallel processing to speed it up. These are somewhat advanced tools and they can be quite hard to make work – you may need to change your code quite a bit. In general, this is only worth doing if/when you do heavy computation on extensive data.

## Packaging

Take some of your previous code and wrap it up into a package.

If you're unfamiliar with creating Python modules and packages, go through this tutorial: [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/).

Next, turn it into an installable package by following one of these tutorials:
* Tutorial: [Packaging Python Projects - Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-build-backend)
* Tutorial: [Python packaging 101](https://www.pyopensci.org/python-package-guide/tutorials/intro.html)

Finally, try to install it into one of your environments, either as an editable install using the `-e` flag (in which case changes to the code are immediately reflected in the importing code), or as a proper built installation. As an example, you can see my [bumpy-banana](https://github.com/neago/bumpy-banana) dummy package.

If you wish, you could also try publishing to the Python packaging index (PyPI).

Instructions for using uv to build a package are [here](https://docs.astral.sh/uv/guides/package/).