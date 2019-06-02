import matplotlib.pyplot as plt
import math

'''
# calculate the coeffiecients -> a, b
y_cap = a + bx
b = sum( (x - x_mean)(y - y_mean) ) / sum ((x-x_mean)**2)
a = y_mean - b * x_mean
'''

def separateVariablesFromSequence(dataset):
    x = list()
    y = list()
    for r in dataset:
        x.append(r[0])
        y.append(r[1])
    return x, y


def calculateMean(input):
    sum = 0
    for i in range(len(input)):
        sum += input[i]
    return sum / float(len(input))


# cov = sum( (x - x_mean)(y - y_mean) )
# var = sum ((x-x_mean)**2)
def calculateVarianceAndCovariance(x, y, x_mean, y_mean):
    cov = 0
    var = 0
    for i in range(len(x)):
        cov += (x[i] - x_mean) * (y[i] - y_mean)
        var += (x[i] - x_mean) ** 2
    return cov, var


def plotTheRegressionLine(x, y, y_pred, pathTosave):
    plt.scatter(x, y, color="r", marker="*", s=30)
    # y_pred = list(map(lambda t : a_coeff + ( b_coeff * t ),x))
    plt.plot(x, y_pred, color='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(pathTosave)

def doThePrediction(testData, a_coeff, b_coeff):
    y_pred = list(map(lambda t: a_coeff + (b_coeff * t), testData))
    return y_pred

def calculateResidual(actual,predicted):
    n = len(actual)
    sum = 0
    for i in range(n):
        sum += (actual[i] - predicted[i]) ** 2
    return sum

def calculateRSME(actual, predicted):
    n = len(actual)
    sum = calculateResidual(actual,predicted)
    return math.sqrt(sum / n)

def calculateVariance(actual,actual_mean):
    var = 0
    for i in range(len(actual)):
        var += (actual[i] - actual_mean) ** 2
    return  var

def getSumOfResidual(actual,predicted):
    sum = 0
    for i in range(len(actual)):
        sum += (actual[i] - predicted[i])
    return sum

def calculateRSquare(actual,predicted,actual_mean):
    residual = calculateResidual(actual,predicted)
    variance = calculateVariance(actual,actual_mean)
    return 1- (residual/variance)

