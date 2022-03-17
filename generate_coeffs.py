import os
import numpy as np
import pyvista as pv
from morphomatics.geom import Surface
from morphomatics.manifold import FundamentalCoords, PointDistributionModel, util
from morphomatics.stats import StatisticalShapeModel

# max number of objects (for debugging and dev)
nObjects=1000
dataPath = "./data/"
# load all data
meshes = []
for (dirpath, dirnames, filenames) in os.walk(dataPath+"AD"):
    for file in filenames:
        if file[-3:] == "obj" and nObjects > len(meshes):
            path = os.sep.join([dirpath, file])
            mesh = pv.read(path)
            meshes.append(mesh)

for (dirpath, dirnames, filenames) in os.walk(dataPath+"CN"):
    for file in filenames:
        if file[-3:] == "obj" and nObjects > len(meshes):
            path = os.sep.join([dirpath, file])
            load = mesh_straight = pv.read(path)
            meshes.append(load)

# to Surface type
as_surface = lambda mesh: Surface(mesh.points, mesh.faces.reshape(-1, 4)[:, 1:])
surfaces = [as_surface(m) for m in meshes]

# construct model
SSM = StatisticalShapeModel(lambda ref: FundamentalCoords(ref)) # replace me with PointDistributionModel
SSM.construct(surfaces)

coeffs = SSM.coeffs.T
#print shape
print("Coeffs Shape: " + str(len(coeffs)) + " " + str(len(coeffs[0])))

# do something with the coeffs
