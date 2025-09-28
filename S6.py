#q1
vector1<-c(10,20,30,10,40,20)
vector2<-c(15,25,35,15,45,25)

data<-data.frame(col1=vector1,cpl2=vector2)

print("Data Frame")
print(data)

duplicates<-duplicated(data)
print("Duplicate Rows:")
print(data[duplicates,])

unique_rows<-unique(data)
print("Unique Rows:")
print(unique_rows)

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