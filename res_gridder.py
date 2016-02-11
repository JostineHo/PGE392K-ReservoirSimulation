import numpy as np
import pandas as pd
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt

data = pd.read_csv('res_depth.csv')
bound = pd.read_csv('bound.csv')
numcols, numrows = 54, 44
x_max = 7322 # ft
y_max = 5753 # ft

# gridding:
xi = np.linspace(-2, x_max, numcols)
yi = np.linspace(-2, y_max, numrows)
xi, yi = np.meshgrid(xi, yi)
x, y, z = data.x.values, data.y.values, data.z.values
zi = griddata(x, y, z, xi, yi, interp='linear')

# masking boundary:
boundx = []
boundy = []
for i in range(len(bound.x)):
    xb = int(bound.x[i]/(x_max/numcols))
    yb = int(bound.y[i]/(y_max/numrows))
    boundx.append(xb)
    boundy.append(yb)

for i in range(1,len(bound.x),2):
    if boundx[i-1] < boundx[i]:
        zi[0:(boundy[i]+1),boundx[i-1]:(boundx[i]+1)] = np.nan
    if boundx[i-1] > boundx[i]:
        zi[(boundy[i]):numrows, (boundx[i]):boundx[i-1]]= np.nan
    elif boundx[i-1] == boundx[i]:
        if boundx[i] < numcols:
            zi[boundy[:],boundx[i-1]:boundx[i]]= np.nan
        else:
            zi[boundy[:], boundx[i]:numcols]= np.nan
            
# plotting:        
plt.style.use('dark_background')
fig, ax = plt.subplots()
p = ax.matshow(zi,interpolation='nearest',cmap='inferno')
# cmap='viridis'
# cmap='inferno'
ax.set_xticks([0,10,20,30,40,50])
ax.set_yticks([0,10,20,30,40])
ax.set_xticklabels([r'0', r'1250', r'2500', r'3750', r'5000', r'6250'])
ax.set_yticklabels([r'0', r'1250', r'2500', r'3750', r'5000'])
ax.set_xlabel('x-direction (ft)', labelpad=12)
ax.xaxis.set_label_position('top')
ax.set_ylabel('y-direction (ft)', labelpad=12)
plt.colorbar(p)
ax.plot(boundx,boundy, 'w', zorder=1, lw = 1)
plt.savefig('deep.png', facecolor="black", edgecolor="none")

# bulk volume calc using thickness:
if np.nanmax(zi) < 1000:
    df = pd.DataFrame(zi)
    sumrows = df[:].sum()
    res_bulk = sumrows[:].sum()*(x_max/numcols)*(y_max/numrows)
    print ('Bulk volume of reservoir: %.2f million ft3' %(res_bulk/1000000))