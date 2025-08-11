# SCIQIS activities 06

## Analyse measurements of squeezed light

In this exercise you will get exposure to a few methods often encountered when processing and analysing experimental data, such as 
* reading and writing data from/to disk
* handling proprietary data formats
* visually inspecting data to understand what they tell
* "massaging" data to bring out the features you're looking for (in a rigorous, responsible way, of course)
* doing spectral analysis of time-series data
* curve-fitting


1. Download data from [this Dropbox link](https://www.dropbox.com/scl/fo/1dxu97vp9f7vioe9atj7g/AOiqbbVhRn-iOqWwHyzwkZQ?rlkey=qpuxehyvenzmyl7747byxnu15&dl=0) and put them somewhere near your sciqis environment (probably best not to put it inside the git repository itself). These are (partial) data from the papers [Compact, low-threshold squeezed light source](https://opg.optica.org/abstract.cfm?uri=oe-27-26-37877) by Jens Arnbak et al., and [Distributed quantum sensing in a continuous-variable entangled network](https://www.nature.com/articles/s41567-019-0743-x) by Xueshi Guo et al. (the full dataset for the latter paper is on [DTU Data](https://doi.org/10.11583/DTU.9988805.v1)).
2. The sciqis repository now contains a tiny single-file package `lecroy` that I wrote to load binary data saved from Lecroy-branded oscilloscopes (the .trc files you will find in the downloaded data). You can find the file [here](https://github.com/qpit/jonas-qopt/blob/master/qopt/lecroy.py) and can in principle just download it and place it next to the tutorial notebook (don't install the entire qopt package – I haven't made it compatible with newer NumPy versions). However, it may be cleaner to install it into your environment by
    ```
    uv pip install -e course_material/lecroy/
    ````
    with the path optionally modified to fit the path relationship between your working environment and the sciqis environment.
3. Spend 5-10 minutes on reading the introduction in the [Squeezed light data analysis](../tutorials/Squeezed%20light%20data%20analysis.ipynb) notebook and the linked Wikipedia article (if you're not quite sure what squeezed light is).
4. Sit together with your neighbour and go slowly through the notebook. Discuss every single line of code – what does it do and why? It can be useful to inspect the variables and methods e.g. by printing them. Any time you are not sure what a line does or why I wrote it that way, you should ask for me.\
(It could also very well be that I underestimated how difficult it is for you to understand the OPO physics or the formatting of the data or the reasons for processing it the way I do – in that case, I'd also very much like to hear from you.)
5. Investigate the data on your own or with your neighbour, for example the steps suggested below. You are also welcome to investigate the provided data in any other way you find interesting.
    - (Jens:) In Jens' data, load the "5MHz..." files and repackage them into an HDF5 file together with metadata and the power values obtained from the file names.
    - (Jens:) Reproduce the figure `power_scaling.png` (located in the data folder): Calculate the noise variance for each of the traces and do a fit to the model for OPO squeezing variance.
    - (Xueshi:) Load all of Xueshi's data using `lecroy.read()` and repackage them into an HDF5 file.
    - (Xueshi:) On the raw time traces of squeezing and anti-squeezing, try to create and apply a filter that can remove the strong oscillation at around 28 MHz. Look into e.g. `firwin`, `iirwin`, `lfilter` or other methods of `scipy.signal`.
    - (Xueshi:) Calculate the averaged spectra of the data. You can consider each of the {electronic, shotnoise, squeezing, antisqueezing} to have been acquired under constant conditions, so it is okay to average all the traces for each channel. Look into `rfft` and `rfftfreq` of `scipy.fft` and/or `periodogram` and `welch` of `scipy.signal`. Look both at spectra for the individual channels and the sum of the four channels.
    - (Xueshi:) Try to fit the model of OPO squeezing/anti-squeezing to the obtained spectra and extra fitted parameters for $x$, $\eta$, $f_{HWHM}$ and possibly $\theta$ or $\sigma$.
    - (Both:) Above, I had some trouble fitting Jens' spectra. [LMFIT]() is a package for minimisation and curve-fitting that improves on `scipy.optimize`. Try to see if it works better for this case. 
6. Try to emulate an experiment (the squeezed light generation above, or whatever theoretical model you like) by generating noisy data and then analysing that data as if it were real. This can e.g. be useful when testing a data analysis workflow, or for finding the distribution of an estimator through the [parametric bootstrapping method](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)?useskin=vector#Parametric_bootstrap). [This Stack Overflow answer](https://stackoverflow.com/questions/67085963/generate-colors-of-noise-in-python/67127726#67127726) suggests how to "colour" noise, i.e. giving it a certain spectrum.