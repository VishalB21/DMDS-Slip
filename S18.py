#q1
vec <- c(12, 45, 7, 89, 23, 56, 3, 78)

max_val <- max(vec)
min_val <- min(vec)

print(paste("Vector Elements:", toString(vec)))
print(paste("Maximum Value:", max_val))
print(paste("Minimum Value:", min_val))

#q2
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 
# Data 
x = np.array([1,2,3,4,5,6,7,8]).reshape(-1, 1)  
y = np.array([7,14,15,18,19,21,26,23]) 
model = LinearRegression() 
model.fit(x, y) 
b0 = model.intercept_ 
b1 = model.coef_[0] 
y_pred = model.predict(x) 
mse = mean_squared_error(y, y_pred) 
r2 = r2_score(y, y_pred) 
print(f"Estimated intercept (b0): {b0}") 
print(f"Estimated slope (b1): {b1}") 
print(f"Mean Squared Error (MSE): {mse}") 
print(f"R^2 score: {r2}") 