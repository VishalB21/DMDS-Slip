#q1
mat1<-matrix(1:6,nrow=2,ncol=3)
mat2<-matrix(7:12,nrow=2,ncol=3)

print("Matrix1")
print(Matrix1)

print("Matrix2")
print(Matrix2)

sum_mat<-matrix1+matrix2

cat("\n Sum of the Matrixes:\n")
print(sum_mat)

#q2
from sklearn.naive_bayes import CategoricalNB 
from sklearn.preprocessing import LabelEncoder 
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast', 
'Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'] 
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild', 
'Mild','Mild','Hot','Mild'] 
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes', 
'Yes','Yes','No'] 
le_weather = LabelEncoder() 
le_temp = LabelEncoder() 
le_play = LabelEncoder() 
weather_encoded = le_weather.fit_transform(weather)  
temp_encoded = le_temp.fit_transform(temp)          
play_encoded = le_play.fit_transform(play)          
features = list(zip(weather_encoded, temp_encoded)) 
model = CategoricalNB() 
model.fit(features, play_encoded) 
predicted = model.predict([[0, 2]]) 
result = le_play.inverse_transform(predicted) 
print("Prediction for [Overcast, Mild]:", result[0])