##Problem 1
-------
(50 points) The figure shown below is a structural contour map of the Nechelik field in the North Slope of Alaska to denote depth Note that each block in the contour map below is 523ft x 523 ft. The second contour plot is of reservoir thickness.

![Figure 1](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/ContourDepth.png?raw=true)

**_Figure 1. Structural contour map of the Nechelik field._**

![Figure 2](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/ContourThickness.png?raw=true)

**_Figure 2. Reservoir thickness contour map of the Nechelik field._**

Your goal is develop a code to discretize the reservoir into rectangular grid blocks on a Cartesian grid and then assign a thickness and depth to each grid. For now, you can nominally use 54*44 (2376) grids but your code should be flexible enough to allow for any number of grids in the x- and y- directions. In fact, it should also allow for non-uniform grid sizes (but still rectangular/Cartesian).

The first step is to use some sort of digitizing software to extract the depths and thicknesses from the provided contour plots. Note that there are several different free digitizing software on the internet. A simple Matlab add-in called “grabit” can help make determining x and y values of points on contour lines easy.

The values you extract will not be on a regular, Cartesian grid, so the next step is to use a 2D interpolating routine to determine the values on your grid. Matlab has a command called “griddata”, which allows users input sample points to be extrapolated to fit a range of given points. In our case, we need to input the x, y and depth values for a number of points on the given contour lines and extrapolate to all  blocks in the top layer of the reservoir. Do keep in mind that the reservoir itself is not rectangular (boundaries of the reservoir are irregular) so the thickness and depth are undefined in that portion of your rectangular domain.

Some MATLAB files are provided and I also have provided a youtube link which may be helpful (please note that the video is just a guide and not necessarily the solution). https://youtu.be/QIaYKvfC1_k

a.	Please make plots of the (1) reservoir thickness and (1) depth in MATLAB or other visualization software.
b.	Compute the bulk volume of the reservoir. Credit will be given for any answer correct within 10%. 10 points will be deducted for any answer outside of +/- 10% of the correct answer. Include this bulk volume in an answer sheet (page after the cover sheet)

####Solution 1(a)
-------
For Python users, try this web-based plot digitizer: http://arohatgi.info/WebPlotDigitizer/

Click link for [Depth data](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/res_depth.csv), [Thickness data](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/res_thickness.csv), [Reservoir boundary](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/bound.csv)

![Figure 3](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/res_depth_masked.png?raw=true)

**_Figure 3. Irregular domain --reservoir depth (grid mode: 54x44)._**

![Figure 4](https://github.com/JostineHo/PGE392K-ReservoirSimulation/blob/master/res_thickness_masked.png?raw=true)

**_Figure 4. Irregular domain --reservoir thickness (grid mode: 54x44)._**

####Solution 1(b)
-------
Bulk volume of reservoir: 1963.58 million ft3
