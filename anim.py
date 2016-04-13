# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as ani
from mpl_toolkits.mplot3d import Axes3D
import mayavi.mlab as maya
# %matplotlib notebook
# %matplotlib inline

filepath='data.npy'
def make_anim(data, _nx, _ny, _nz):
    #densities = np.load(filepath).reshape((128,128,128))
    densities = np.array(data).reshape((_nx, _ny, _nz))
    title = "Gestosc DFT w iteracji 0"
    xmin = 0
    xmax = _nx
    fig, ax = plt.subplots()
    Title = ax.set_title(title)
    min_value = np.min(densities[:,:,_nz/2])
    max_value = np.max(densities[:,:,_nz/2])
    IM = ax.imshow(densities[:,:,_nz/2], vmin = min_value, vmax = max_value)

    def func(i):
        IM.set_array(densities[:,:,i])
        Title.set_text("Gestosc DFT dla z = %d"%(i))
        return IM, Title

    ax.set_xlim(xmin,xmax)
    ax.set_ylim(xmin,xmax)
    plt.colorbar(IM)
    animation = ani.FuncAnimation(fig, func, frames = _nz, interval=200, repeat = True, repeat_delay = 1500)
    plt.show()
