import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as ani
from mpl_toolkits.mplot3d import Axes3D
import mayavi.mlab as maya
# %matplotlib notebook
# %matplotlib inline
filepath='data.npy'
filepathx='xdata.npy'
filepathy='ydata.npy'
filepathz='zdata.npy'


x = np.load(filepathx).reshape((100,100,100))
y = np.load(filepathy).reshape((100,100,100))
z = np.load(filepathz).reshape((100,100,100))
densities = np.load(filepath).reshape((1,128,128,128))
#density=density.reshape((28,1000000))#.reshape((28,100,100,100))
for density in densities:
	maya.contour3d(x,y,z,density, transparent=True, opacity=0.5, contours=10)
	maya.show()


#print density[-1], density[-1].max()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# sp = ax.scatter(x,y,z, s=20, c=density[-1])
# plt.colorbar(sp)
# plt.show()