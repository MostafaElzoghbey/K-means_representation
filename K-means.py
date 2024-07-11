import math
import matplotlib.pyplot


Iteration = 1


def KmeansClustering(dataSet, k, centroids, clustersBuffer):

    global Iteration

    # if Iteration == 6:

    #     return print("the result clusters:", clustersBuffer)

    print("\n********** Iteration Number:", Iteration, "***********\n")

    Iteration = Iteration + 1

    print("Centroids: ", centroids)
    print()

    dataSetXs = []
    dataSetYs = []

    for i in range(len(dataSet)):

        dataSetXs.append(dataSet[i][0])
        dataSetYs.append(dataSet[i][1])

    matplotlib.pyplot.scatter(dataSetXs, dataSetYs)
    matplotlib.pyplot.scatter(centroids[0][0], centroids[0][1], linewidths=5)
    matplotlib.pyplot.scatter(centroids[1][0], centroids[1][1], linewidths=5)
    matplotlib.pyplot.show()

    distances = []
    temp = []

    for i in range(len(dataSet)):

        temp = []

        for j in range(len(centroids)):

            Distance = float(
                "%.1f"
                % math.sqrt(
                    (dataSet[i][0] - centroids[j][0]) ** 2
                    + (dataSet[i][1] - centroids[j][1]) ** 2
                )
            )
            temp.append(Distance)

        distances.append(temp)

    print("Distances from c1 and c2:\n\n", distances)
    print()

    clusters = []
    temp = []

    for i in range(k):

        temp = []

        for j in range(len(distances)):

            if distances[j].index(min(distances[j])) == i:

                temp.append(j)

        clusters.append(temp)

    print("Clusters:\n\n", clusters)
    print()

    if clusters == clustersBuffer:

        return print("\nThe result clusters:\n\n", clusters, "\n")

    clustersBuffer = clusters

    centroids = []
    temp = []
    sumX = 0
    sumY = 0

    for i in range(len(clusters)):

        temp = []
        sumX = 0
        sumY = 0

        for j in range(len(clusters[i])):

            sumX += dataSet[clusters[i][j]][0]
            sumY += dataSet[clusters[i][j]][1]

        if len(clusters[i]) > 0:

            MeanX = sumX / len(clusters[i])
            temp.append(int(MeanX))
            MeanY = sumY / len(clusters[i])
            temp.append(int(MeanY))
            centroids.append(temp)

        else:

            centroids.append([0, 0])

    print("NewCentroids: ", centroids)
    print()

    return KmeansClustering(dataSet, k, centroids, clustersBuffer)


dataSet = [
    [12, 10],
    [11, 8],
    [13, 9],
    [10, 11],
    [10, 8],
    [10, 11],
    [13, 14],
    [6, 7],
    [10, 10],
    [10, 9],
    [2, 1],
    [6, 3],
    [5, 5],
    [6, 4],
    [1, 2],
    [4, 3],
]

k = 2

centroids = [[2, 4], [5, 5]]

KmeansClustering(dataSet, k, centroids, [])
