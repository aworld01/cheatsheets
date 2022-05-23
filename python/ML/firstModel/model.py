import pandas as pd

## step - 1 _________Datasets or Data_preparation
file="House Pricing.csv"
file_data=pd.read_csv(file)
file_data.columns
data=file_data.dropna(axis=0)

## step - 2 _________Labels & Features
y=data.Price #Labels
data_features=['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] #Features
x=data[data_features]

## step - 3 _________Creating the Model
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(random_state=1)
model.fit(x, y)

## step - 4 _________Testing
d=x.head() #to take random five houses.
print("These are the houses:-")
print(d)
p=model.predict(x.head()) #to predict random five houses price.
print("These are the prices of houses:-")
print(p)

## Time step= 50:00/2:39:19
