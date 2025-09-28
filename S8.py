#q1
fibonacci <- numeric(10)   
fibonacci[1] <- 0
fibonacci[2] <- 1

for (i in 3:10) {
  fibonacci[i] <- fibonacci[i-1] + fibonacci[i-2]
}

print(fibonacci)

#q2
import pandas as pd 
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.cluster import KMeans 
df = pd.read_csv("CC GENERAL.csv") 
df = df.drop(columns=["CUST_ID"]) 
imputer = SimpleImputer(strategy="median") 
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns) 
scaler = MinMaxScaler() 
df_scaled = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df.columns) 
kmeans = KMeans(n_clusters=5, random_state=42) 
df_scaled["Cluster"] = kmeans.fit_predict(df_scaled) 
df["Cluster"] = df_scaled["Cluster"] 
print(df["Cluster"].value_counts()) 