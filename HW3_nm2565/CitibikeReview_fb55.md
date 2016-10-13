Before getting to the Null in a project where you choose what to work on you should tell us why your question is interesting and worth asking and  give a rationale for why you would expect to see an effect.

In the Null and alternative hypothesis quantifiable metrics have to be used. Trip duration is not quantifiable for a set of >1 user: you need to state if you want the mean, median or whatever measure of trip duration for the samples you gave.
The Null hypothesis properly formulated in words and formulae otherwise.


Data MUST BE MOVED FROM THE LOCAL DIRECTORY TO THE PUIDATA DIRECTORY.
 You are checking if PUIDATA is a defined env variable (twice...) but you do not anything with it and you keep the data in the ocal directory. That is a bad habit (for a number of reasons). Data should be stored separately from code. In our case in the $PUIDATA directory.


For us this protects the TAs from having replicae of data all over their home directory.

EVERY FIGURE NEEDS ITS OWN CAPTION!

citibike.head is a function:
citibike.head()

If used not as a function it will dump a lot of lines non formatted. if used properly it will print the first 5 lines in a tabulated format. Much better!




Your last figure is completely uninformative because such a large fraction of the data falls in a single min that the other bins are literally invisible. you have two options: show the data in a log plot. or cut the top trip durations as outliers (for example the top x% or what exceeds a predefined threshold)



What are the units of trip duration?? always state which units you work in and put them in the plot labels

Histogram is not a proper title for a plot: "Histogram of age...."


Only once you have decided what you want to measure (mean, median, fraction above threshold...) you can decide which test you want to do.


