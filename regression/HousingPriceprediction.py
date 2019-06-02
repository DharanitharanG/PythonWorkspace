import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston
house = load_boston()


# print(type(house))
#
# print(house.keys())
# print(house.data.shape)
# print(house.feature_names)
# print(house.DESCR)


house_data = pd.DataFrame(house.data)
house_data.columns = house.feature_names
print(house_data.head())

print(house.target[:5])
house_data['price'] = house.target

print(house_data.head())


from sklearn.linear_model import LinearRegression
x = house_data.drop('price',axis=1)
print(x)
lm = LinearRegression()
lm

print(lm.fit(x,house_data.price))

print(x.columns)

print("Intercept : ",lm.intercept_)
print("coefficients :",lm.coef_)

print("zip(x.columns,lm.coef_)", zip(x.columns,lm.coef_))

coeff = pd.DataFrame(zip(x.columns,lm.coef_),columns=['features','estimatedcoefficients'])
print(coeff)

plt.scatter(house_data.RM,house_data.price)
plt.xlabel("RM")
plt.ylabel("housing price")
plt.title("Relationship between RM & price")
plt.show()

print(lm.predict(x)[0:5])

plt.scatter(house_data.price,lm.predict(x))
plt.xlabel("Prices ")
plt.ylabel("predicted price")
plt.title("prices vd predicted price")
plt.show()

mse = np.mean((house_data.price - lm.predict(x))**2)

print (mse)

lm = LinearRegression()
lm.fit(x[['PTRATIO']],house_data.price)


mse2 = np.mean((house_data.price  - lm.predict(x[['PTRATIO']]))**2)
print (mse2)

# mse is measure of how close a fitted line is to data
# The smaller the mean square error, the closer the fit is to data

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,house_data.price,test_size=0.33)

print (x_train.shape)
print (x_test.shape)
print (y_train.shape)
print (y_test.shape)


lm = LinearRegression()
lm.fit(x_train,y_train)

pred_train = lm.predict(x_train)
pred_test = lm.predict(x_test)


print(pred_train)



mse_y_train = np.mean(((y_train - lm.predict(x_train)))**2)
mse_y_test = np.mean((y_test-lm.predict(x_test))**2)

print(mse_y_train)
print(mse_y_test)




























