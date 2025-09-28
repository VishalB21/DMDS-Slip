#q1
list1 <- list("x", "y", "z")
list2 <- list("X", "Y", "Z", "x", "y", "z")

vec1 <- unlist(list1)
vec2 <- unlist(list2)

diff1 <- setdiff(vec1, vec2)

diff2 <- setdiff(vec2, vec1)

print("Elements in list1 but not in list2:")
print(diff1)

print("Elements in list2 but not in list1:")
print(diff2)

#q2
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.cluster import AgglomerativeClustering 
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage 
df = pd.read_csv("Customers.csv") 
print(df.head()) 

df_numeric = df.select_dtypes(include=[np.number])  
df_numeric = df_numeric.fillna(df_numeric.median()) 
scaler = MinMaxScaler() 
data_scaled = scaler.fit_transform(df_numeric) 
linked = linkage(data_scaled, method='ward') 
plt.figure(figsize=(10, 7)) 
dendrogram(linked, 
orientation='top', 
distance_sort='descending', 
show_leaf_counts=False) 
plt.title('Dendrogram') 
plt.xlabel('Samples') 
plt.ylabel('Distance') 
plt.show() 
n_clusters = 3 
agg_clust = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward') 
labels = agg_clust.fit_predict(data_scaled) 
df['Cluster'] = labels 
print(df['Cluster'].value_counts()) 
df.to_csv("Customer_with_clusters.csv", index=False) 
