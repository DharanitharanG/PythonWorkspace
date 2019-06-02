import linearreg.LinearRegressionFunctions as lf
# from linearreg.LinearRegressionFunctions import separateVariablesFromSequence

# dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
dataset = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
x,y = lf.separateVariablesFromSequence(dataset)
x_mean = lf.calculateMean(x)
y_mean = lf.calculateMean(y)
variances = lf.calculateVarianceAndCovariance(x,y,x_mean,y_mean)
b_coeff = variances[0]/variances[1]
a_coeff = y_mean - (b_coeff * x_mean)
y_pred = lf.doThePrediction(x,a_coeff,b_coeff)
lf.plotTheRegressionLine(x,y,y_pred,"/home/dharani/LinearReg.png")
rsme = lf.calculateRSME(y,y_pred)
r_square = lf.calculateRSquare(y,y_pred,y_mean)
sumOfResidual = lf.getSumOfResidual(y,y_pred);

print("***** LINEAR REGRESSION CALCULATIONS *****\n")
print("The dataset is : ",dataset)
print("x is : ",x)
print("y is : ",y)
print("x_mean : ",x_mean,"\ny_mean : ",y_mean)
print("The coefficient b is : ",b_coeff)
print("The coefficient a is : ",a_coeff)
print("Hence, the regression line is :: y=",a_coeff ,"+",b_coeff,"x")
print("The sum of residual is : ",sumOfResidual)
print("The RSME is : ",rsme)
print("The R Square value is : ",r_square)

