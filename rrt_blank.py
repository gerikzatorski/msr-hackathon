#!/usr/bin/env python
import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches


FNAME = "N_map.png"
world = imread(FNAME)
world = np.flipud(world)
Xmax = world.shape[0]
Ymax = world.shape[1]
fig = mp.figure()
ax = fig.add_subplot(111)
mp.imshow(world, cmap=mp.cm.binary, interpolation='nearest', origin='lower', extent=[0,Xmax,0,Ymax])
ax.set_xlim([-1.5,1.5])
ax.set_ylim([-1.5,1.5])
fig.show()

def drawLine(p1, p2):
    path = Path([[p1[0],p2[1]],[p2[0],p2[1]]], [Path.MOVETO,Path.LINETO])
    patch = patches.PathPatch(path)
    ax.add_patch(patch)
