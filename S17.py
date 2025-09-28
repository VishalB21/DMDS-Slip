#q1

fibonacci <- numeric(20)   
fibonacci[1] <- 0
fibonacci[2] <- 1

for (i in 3:20) {
  fibonacci[i] <- fibonacci[i-1] + fibonacci[i-2]
}

print("First 20 Fibonacci Numbers:")
print(fibonacci)

#q2
import pandas as pd 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 
import numpy as np 
 
# Data 
Stock_Market = { 
    'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017, 
             2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016], 
    'Month': [12,11,10,9,8,7,6,5,4,3,2,1, 
              12,11,10,9,8,7,6,5,4,3,2,1], 
    'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2, 
                      2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75], 
    'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9, 
                          6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1], 
    'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167, 
                          1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719] 
} 
 
df = pd.DataFrame(Stock_Market) 
 
X = df[['Year', 'Month', 'Interest_Rate', 'Unemployment_Rate']] 
y = df['Stock_Index_Price'] 
 
model = LinearRegression() 
model.fit(X, y) 
 
print("Intercept:", model.intercept_) 
print("Coefficients:", list(zip(X.columns, model.coef_))) 
 
plt.figure(figsize=(8,5)) 
plt.scatter(df['Interest_Rate'], y, color='blue', label='Actual Data') 
 
interest_rate_range = np.linspace(df['Interest_Rate'].min(), df['Interest_Rate'].max(), 
100) 
mean_year = df['Year'].mean() 
mean_month = df['Month'].mean() 
mean_unemployment = df['Unemployment_Rate'].mean() 
X_plot = pd.DataFrame({ 
'Year': [mean_year]*100, 
'Month': [mean_month]*100, 
'Interest_Rate': interest_rate_range, 
'Unemployment_Rate': [mean_unemployment]*100 
}) 
predicted_prices = model.predict(X_plot) 
plt.plot(interest_rate_range, predicted_prices, color='red', label='Regression Line') 
plt.xlabel('Interest Rate') 
plt.ylabel('Stock Index Price') 
plt.title('Stock Index Price vs Interest Rate') 
plt.legend() 
plt.grid(True) 
plt.show()