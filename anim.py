# -*- coding: utf-8 -*-
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
densities = np.load(filepath).reshape((28,100,100,100))


title = "Gestosc DFT w iteracji 0"

xmin = 20
xmax = 80
fig, ax = plt.subplots()
Title = ax.set_title(title)
min_value = np.min(densities[:,:,:,50])
max_value = np.max(densities[:,:,:,50])
IM = ax.imshow(densities[0,:,:,50], vmin = min_value, vmax = max_value)
def func(i):
	IM.set_array(densities[i,:,:,50])
	Title.set_text("Gestosc DFT w iteracji %d"%i)
	return IM, Title

ax.set_xlim(xmin,xmax)
ax.set_ylim(xmin,xmax)
plt.colorbar(IM)
animation=ani.FuncAnimation(fig, func, frames = 28, interval=100, repeat = True, repeat_delay = 1500)
plt.show()

#print density[-1], density[-1].max()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# sp = ax.scatter(x,y,z, s=20, c=density[-1])
# plt.colorbar(sp)
# plt.show()