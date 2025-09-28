#q1
factor1<-factor(c("apple","banana","apple"))
factor2<-factor(c("orange","banana","grape"))

concated_factor<-factor(c(as.character(factor1)as.character(factor2)))

print(concated_factor)
print(levels(concated_factor))

#q2
import numpy as np 
from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import classification_report, accuracy_score 
from sklearn.preprocessing import Binarizer 
data = load_diabetes() 
X = data.data 
y_regression = data.target 
 
threshold = np.median(y_regression) 
y = Binarizer(threshold=threshold).fit_transform(y_regression.reshape(-1, 1)).ravel() 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
clf = DecisionTreeClassifier(random_state=42) 
clf.fit(X_train, y_train) 
y_pred = clf.predict(X_test) 
print("Accuracy:", accuracy_score(y_test, y_pred)) 
print("\nClassification Report:\n", classification_report(y_test, y_pred)) 
