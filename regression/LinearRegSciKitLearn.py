import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression

x = [1,2,3,4,5]
y = [2,3,4,5,6]


lm = LinearRegression()
lm.fit(pd.DataFrame(x),y)

print(lm.intercept_)
print(lm.coef_)

plt.scatter(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Relationship between X & Y")
plt.show()





