# generate related variables
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import pandas as pd

# seed random number generator
# seed(1)
# prepare data
# data1 = 20 * randn(1000) + 100
# data2 = data1 + (10 * randn(1000) + 50)

data1 = [1,2,3,4,5,6]
data2 = [2,3,4,5,6,7]
list2 = zip(data1,data2)
df = pd.DataFrame(list2,columns=['X','Y'])
print(df.corr())
# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
# plot
pyplot.scatter(data1, data2)
pyplot.show()

# cov(X, Y) = (sum(x - mean(X)) * (y - mean(Y))) * 1 / (n - 1)
# calculate covariance matrix
from numpy import cov
covariance = cov(data1, data2)
print(covariance)


# Pearson's correlation coefficient =
# covariance(X, Y) / (stdv(X) * stdv(Y))
from scipy.stats import pearsonr
corr, p_val = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)
print('p_val is ',p_val)














