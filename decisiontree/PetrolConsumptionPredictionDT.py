import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

petrol_data = pd.read_csv("/home/dharani/Downloads/petrol_consumption.csv")

# print(petrol_data.head(5))
print(petrol_data.describe())
X = petrol_data.drop('Petrol_Consumption', axis=1)
y = petrol_data['Petrol_Consumption']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})

print(df)

