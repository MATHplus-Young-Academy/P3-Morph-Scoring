import os
import sys
import inspect
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
from sklearn.preprocessing import normalize
from utils import runSVMClassification, plotClassificationResults

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from morphomatics_med.geom import Surface
from morphomatics_med.manifold import FundamentalCoords, PointDistributionModel, util
from morphomatics_med.stats import StatisticalShapeModel

median = np.load("./mesh_median.npy")
mean = np.load("./mesh_mean.npy")

#load faces indices
mesh = pv.read("./data/AD/test/10064.obj")

# align
from morphomatics_med.manifold.util import align

median = align(median, mean)

# calculate difference
diff = np.linalg.norm(median - mean, axis = 1)
print(diff.shape)

pl = pv.Plotter()
pl.add_mesh(pv.PolyData(median, mesh.faces), smooth_shading=True, scalars = diff, cmap = "viridis")
pl.view_yx()
pl.camera.roll += 180
pl.show()
