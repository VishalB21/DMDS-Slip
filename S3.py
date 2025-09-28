#q1
num=123
sum=0
rev=0
while(num>0)
{
    r=num%10
    sum=sum+r 
    rev=rev*10+r 
    num=num%1%10
}
print(paste("Reverse Number is :",rev))
print(paste("Sum of digit is:",sum))

#q2
import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18]) 
x_mean = np.mean(x) 
y_mean = np.mean(y) 
b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2) 
b0 = y_mean - b1 * x_mean 
print(b0, b1) 
y_pred = b0 + b1 * x 
plt.scatter(x, y, color='blue', label='Original data') 
plt.plot(x, y_pred, color='red', label='Regression line') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Simple Linear Regression') 
plt.legend() 
plt.grid(True) 
plt.show() 