#q1
a=c(10,20,30,40)
b=c(20,30,40,50)
print("Original Vectors")
print(a)
print(b)
print("After Calculation")
print(a+b)
print(a*b)
print(a/b)

#q2
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree 
import matplotlib.pyplot as plt 
df = pd.read_csv("shows.csv") 
df['Nationality'] = df['Nationality'].map({'UK': 0, 'USA': 1, 'N': 2}) 
df['Go'] = df['Go'].map({'YES': 1, 'NO': 0}) 
features = ['Age', 'Experience', 'Rank', 'Nationality'] 
X = df[features] 
y = df['Go'] 
dtree = DecisionTreeClassifier() 
dtree = dtree.fit(X, y) 
plt.figure(figsize=(10, 6)) 
tree.plot_tree(dtree, feature_names=features, class_names=["NO", "YES"], 
filled=True) 
plt.savefig("tree.png") 
print("tree.png has been saved in your current directory.")