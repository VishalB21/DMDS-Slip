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
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error, mean_squared_error 
df = pd.read_csv('student_scores.csv')  # adjust filename if needed 
print(df.head()) 

X = df[['Hours']].values  
y = df['Scores'].values            
model = LinearRegression() 
model.fit(X, y) 
y_pred = model.predict(X) 
mae = mean_absolute_error(y, y_pred) 
mse = mean_squared_error(y, y_pred) 
rmse = np.sqrt(mse) 
print("Mean Absolute Error (MAE):", mae) 
print("Mean Squared Error (MSE):", mse) 
print("Root Mean Squared Error (RMSE):", rmse)