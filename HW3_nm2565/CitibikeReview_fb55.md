In the Null and alternative hypiothesis quantifiable metricss have to be used. trip duration is not quantifiable for a set of >1 user: you need to state if you want the mean, median or whatever measure of trip duration for the samples you gave.
The Null hypothesis properly formulated in words and formulae otherwise.

Your data *may* support the question but you have not yet extracted ages from birth years, so we still do not know.


Please make sure your lines of code (and comments) are not too long! the code should be contained in a cell for jupyter notebooks, not force the cell to expand horizontally. pep8 recommands <77 (or something like that) characters


Before you state your hypothesis you shoudl give a rationale for why you would expect to see an effect.

Data MUST BE MOVED FROM THE LOCAL DIRECTORY TO THE PUIDATA DIRECTORY.

It is not generally a good habit to mix data and code in the same dir.

For us this protects the TAs from having replicae of data all over their home directory.

EVERY FIGURE NEEDS ITS OWN CAPTION!

What are the units of trip duration?? always state which units you work in and put them in the plot labels

Histogram is not a proper title for a plot: "Histogram of age...."

Your last figure is completely uninformative because such a large fraction of the data falls in a single min that the other bins are literally invisible. you have two options: show the data in a log plot. or cut the top trip durations as outliers (for example the top x% or what exceeds a predefined threshold)


Only once you have decided what you want to measure (mean, median, fraction above threshold...) you can decide which test you want to do.

citibike.head is a function:
citibike.head()

If used not as a function it will dump a lot of lines non formatted. if used properly it will print the first 5 lines in a tabulated format. Much better!

