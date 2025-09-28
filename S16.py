#q1
year <- c("2001", "2002", "2003")
export <- c(26, 32, 35)
import <- c(35, 40, 50)
data <- rbind(export, import)
barplot(data,
        beside = TRUE,                     
        names.arg = year,                 
        col = c("skyblue", "orange"),      
        main = "Export and Import (2001–2003)",
        xlab = "Year",
        ylab = "Value")
legend("topright",
       legend = c("Export", "Import"),
       fill = c("skyblue", "orange"))


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
