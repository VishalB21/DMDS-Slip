#q1
emp_id   <- c(101, 102, 103, 104, 105)
emp_name <- c("John", "Emma", "Raj", "Sophia", "Amit")
department <- c("HR", "Finance", "IT", "Marketing", "Sales")
salary   <- c(45000, 55000, 60000, 50000, 48000)
experience <- c(2, 5, 3, 4, 2)

employees <- data.frame(
  ID = emp_id,
  Name = emp_name,
  Department = department,
  Salary = salary,
  Experience = experience
)

print("Employee Data Frame:")
print(employees)

print("Summary of Employee Data:")
summary(employees)

#q2 Cancer wala
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm_model = SVC(kernel='linear', random_state=42)

svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("SVM Model Performance on Cancer Dataset")
print("----------------------------------------")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))
