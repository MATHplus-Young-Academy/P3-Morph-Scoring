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

from test import say
from morphomatics_med.geom import Surface
from morphomatics_med.manifold import FundamentalCoords, PointDistributionModel, util
from morphomatics_med.stats import StatisticalShapeModel

# generate labels the stupid way
labels = []
dataPath = "./data/"
for (dirpath, dirnames, filenames) in os.walk(dataPath+"AD"):
    for file in filenames:
        if file[-3:] == "obj":
            labels.append(0);

for (dirpath, dirnames, filenames) in os.walk(dataPath+"CN"):
    for file in filenames:
        if file[-3:] == "obj":
            labels.append(1)
labels = np.array(labels)

medianCoeffs = np.load("./coeffs_median.npy")
meanCoeffs = np.load("./coeffs_mean.npy")

# do something with the coeffs
nPartitions = 19
nRandomSamplings = 20000

[nR1, nR2] = [0, len(medianCoeffs)] # e.g. [0, 114] (full range), [0, 3], [105, 114], etc.
# dark green (FCM) and dark violet (PDM)
colors = ['#008c04', '#ae00d8']

# normalize feature vectors
medianCoeffNorm = normalize(medianCoeffs[nR1:nR2, :], axis=0, norm="l2")
medianAvgAccuracyPerPartition, medianStdDevPerPartition = runSVMClassification(nPartitions, nRandomSamplings, medianCoeffNorm, labels)
# normalize feature vectors
meanCoeffNorm = normalize(medianCoeffs[nR1:nR2, :], axis=0, norm="l2")
meanAvgAccuracyPerPartition, meanStdDevPerPartition = runSVMClassification(nPartitions, nRandomSamplings, meanCoeffNorm, labels)

np.save("data/classification/avg_median", medianAvgAccuracyPerPartition)
np.save("data/classification/std_median", medianStdDevPerPartition)
np.save("data/classification/avg_mean", meanAvgAccuracyPerPartition)
np.save("data/classification/std_mean", meanStdDevPerPartition)

# compare two different approaches
data_list_avg = [meanAvgAccuracyPerPartition,medianAvgAccuracyPerPartition]
data_list_std = [meanStdDevPerPartition,medianStdDevPerPartition]
names = ["Mean", "Median"]

plotClassificationResults(data_list_avg, data_list_std, plt, colors, names, "Alzheimer Classification - Mean vs. Median")
