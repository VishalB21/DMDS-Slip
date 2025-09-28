#q1
rollno   <- c(1, 2, 3, 4, 5)
studname <- c("Rahul", "Priya", "Amit", "Sneha", "Karan")
address  <- c("Pune", "Mumbai", "Delhi", "Nagpur", "Bhopal")
marks    <- c(85, 92, 76, 88, 95)

students <- data.frame(
  RollNo = rollno,
  StudName = studname,
  Address = address,
  Marks = marks,
  stringsAsFactors = FALSE
)

print("Student Details:")
print(students)

#q2
import pandas as pd 
from sklearn import linear_model 
import matplotlib.pyplot as plt 

data = { 
'Weight': [2300, 2500, 2700, 3000, 3200, 3400, 3600, 3800, 4000, 4200], 
'Volume': [1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200], 
'CO2':    [99, 100, 103, 105, 107, 109, 110, 113, 115, 117] 
} 
df = pd.DataFrame(data) 
X = df[['Weight', 'Volume']]  
y = df['CO2']                 
 
model = linear_model.LinearRegression() 
model.fit(X, y) 
print("Intercept:", model.intercept_) 
print("Coefficients:", model.coef_)  
predicted_co2 = model.predict([[3300, 1800]]) 
print(f"Predicted CO2 for Weight=3300 & Volume=1800: {predicted_co2[0]:.2f}")