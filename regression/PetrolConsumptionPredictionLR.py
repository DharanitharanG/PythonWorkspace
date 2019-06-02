import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression

petrol_data = pd.read_csv("/home/dharani/Downloads/petrol_consumption.csv")

# print(petrol_data.head(5))
print(petrol_data.describe())
X = petrol_data.drop('Petrol_Consumption', axis=1)
y = petrol_data['Petrol_Consumption']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

lm = LinearRegression()

modl = lm.fit(X,y)

import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

print(lm.fit(X,y))

print(X.columns)

print("Intercept : ",lm.intercept_)
print("coefficients :",lm.coef_)

print("zip(x.columns,lm.coef_)", zip(X.columns,lm.coef_))

coeff = pd.DataFrame(zip(X.columns,lm.coef_),columns=['features','estimatedcoefficients'])
print(coeff)
