import numpy as np
from sklearn import svm
from sklearn.model_selection import StratifiedShuffleSplit

def trainAndPredictSVM(train_index, test_index, features, labels):

    lsvm = svm.LinearSVC()
    lsvm.fit(features[:, train_index].transpose(), labels[train_index])
    predictedTLabels = lsvm.predict(features[:, test_index].transpose())

    return predictedTLabels, labels[test_index]

def classifyMultipleTimes(part, nRandomSampling, features, labels):
    accuracyPerSampling = np.empty([nRandomSampling])
    sss = StratifiedShuffleSplit(n_splits=nRandomSampling, train_size=part)
    for j, [train_index, test_index] in enumerate(sss.split(features.transpose(), labels)):
        predictedTLabels, testLabels = trainAndPredictSVM(train_index, test_index, features, labels)
        accuracyPerSampling[j] = 1.0 - np.count_nonzero(testLabels - predictedTLabels)/predictedTLabels.shape[0]
        #if j % 50 == 0:
        #    print(f'Random sampling  {j}  ({nRandomSampling})')

    return accuracyPerSampling

def runSVMClassification(nPartition, nRandomSamplings, features, labels):
    avgAccuracyPerPartition = np.empty([nPartition])
    stdDevPerPartition = np.empty([nPartition])
    for lp in range(1, nPartition + 1):
        accuracyPerSampling = classifyMultipleTimes(lp / (nPartition + 1), nRandomSamplings, features, labels)
        avgAccuracyPerPartition[lp - 1] = np.mean(accuracyPerSampling)
        stdDevPerPartition[lp - 1] = np.std(accuracyPerSampling)
        print(f'Part  {lp}  ({nPartition})')

    return avgAccuracyPerPartition, stdDevPerPartition


def plotClassificationResults(data_list_avg, data_list_std, plt, colors, names, title):
    data_list_std_high = [data_list_avg[0] + data_list_std[0], data_list_avg[1] + data_list_std[1]]

    # cut off at 1.0
    data_list_std_high[0][data_list_std_high[0] > 1.0] = 1.0
    data_list_std_high[1][data_list_std_high[1] > 1.0] = 1.0
    data_list_std_low = [data_list_avg[0] - data_list_std[0], data_list_avg[1] - data_list_std[1]]

    label_list = names

    x = [100 * lp / (len(data_list_avg[0]) + 1) for lp in range(1, len(data_list_avg[0]) + 1)]
    plt.figure(figsize=(12, 7))
    for k in range(2):
        plt.plot(x, data_list_avg[k], linestyle='-', marker='o', color=colors[k], label=label_list[k], lw=3, ms=12)
        # some kind of whisker bars showing the standard deviation around the average
        plt.vlines(x=x, ymin=data_list_std_low[k], ymax=data_list_std_high[k], colors=colors[k], lw=1.5)
        plt.scatter(x, data_list_std_low[k], marker='_', color=colors[k], lw=1.5)
        plt.scatter(x, data_list_std_high[k], marker='_', color=colors[k], lw=1.5)

    plt.title(title)
    plt.legend(loc='lower right')
    plt.xlabel('% of data for training')
    plt.ylabel('accuracy')
    plt.xticks(range(0, 101, 10))

    plt.savefig(title+ ".png", dpi = "figure");

    plt.show()
