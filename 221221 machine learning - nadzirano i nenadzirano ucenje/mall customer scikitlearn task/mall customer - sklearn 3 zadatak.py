#Mijenjajte broj klastera, te grafički prikažite ovisnost kriterijske funkcije o broju klastera.

import io
import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def show_clusters(points, cluster_labels):
    first_cluster_points = []
    second_cluster_points = []
    third_cluster_points = []


    for i in range(len(cluster_labels)):
        cluster_index = cluster_labels[i]
        if cluster_index == 0:
            first_cluster_points.append(points[i])
        elif cluster_index == 1:
            second_cluster_points.append(points[i])
        elif cluster_index == 2:
            third_cluster_points.append(points[i])

    first_cluster_points_x = [point[0] for point in first_cluster_points]
    first_cluster_points_y = [point[1] for point in first_cluster_points]

    second_cluster_points_x = [point[0] for point in second_cluster_points]
    second_cluster_points_y = [point[1] for point in second_cluster_points]

    third_cluster_points_x = [point[0] for point in third_cluster_points]
    third_cluster_points_y = [point[1] for point in third_cluster_points]

    plt.scatter(first_cluster_points_x, first_cluster_points_y, c='red')
    plt.scatter(second_cluster_points_x, second_cluster_points_y, c='blue')
    plt.scatter(third_cluster_points_x, third_cluster_points_y, c='yellow')
    plt.show()

data=pd.read_csv('Mall_Customers.csv')

X=data.iloc[:,[3,4]].values

def drawSSEPlot(df, column_indices, n_clusters=30, max_iter=300, tol=1e-04, init='k-means++', n_init=10, algorithm='auto'):
    import matplotlib.pyplot as plt
    inertia_values = []
    for i in range(1, n_clusters+1):
        km = KMeans(n_clusters=i, max_iter=max_iter, tol=tol, init=init, n_init=n_init, random_state=1, algorithm=algorithm)
        km.fit_predict(df.iloc[:, column_indices])
        inertia_values.append(km.inertia_)
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(range(1, n_clusters+1), inertia_values, color='red')
    plt.xlabel('No. of Clusters', fontsize=15)
    plt.ylabel('SSE / Inertia', fontsize=15)
    plt.title('SSE / Inertia vs No. Of Clusters', fontsize=15)
    plt.grid()
    plt.show()

df = pd.DataFrame(X)

drawSSEPlot(df, [0, 1])