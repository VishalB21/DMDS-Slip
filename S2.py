#q1
mul<-function(number,limit=10){
    for (i in 1:limit){
        result<-number*isinstance
        cat(number,"*",i,"=",result,"\n")
    }
}
mul(5)

#q2
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs 
from sklearn.cluster import KMeans 
n_samples = 300 
n_features = 2 
n_clusters = 4 
random_state = 42 
X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, 
random_state=random_state) 
plt.scatter(X[:, 0], X[:, 1], c='gray', s=30) 
plt.title("Synthetic Dataset") 
plt.xlabel("Feature 1") 
plt.ylabel("Feature 2") 
plt.show() 
kmeans = KMeans(n_clusters=n_clusters, random_state=random_state) 
kmeans.fit(X) 
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', s=30) 
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', 
s=200, label='Centroids') 
plt.title("K-Means Clustering") 
plt.xlabel("Feature 1") 
plt.ylabel("Feature 2") 
plt.legend() 
plt.show() 