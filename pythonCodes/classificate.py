import pandas as pd 
from sklearn.tree import DecisionTreeRegressor as dt
from sklearn.metrics import mean_absolute_error as me # for calculating errors
from sklearn.ensemble import RandomForestRegressor as rf #another model
iris_data = pd.read_csv('iris.csv')
#print(iris_data.columns)
# now defining x and y for y = mx + c + E(epsilon) 
x=iris_data[['sepal length','sepal width','petal length','petal width']] 
y=iris_data[['category']]
#print(y)
# selecting the model
mymodel = dt()
# training the machine
mymodel.fit(x,y)
#print(x.head())
#pridicting the values
print(mymodel.predict(x.head()))
predicted_y = mymodel.predict(x)
# getting error with test data so that it can be included and ans. become more accurate
print(me(y,predicted_y))



# randomforest model
myforest = rf()
myforest.fit(x,y)
print(myforest.predict(x.head()))