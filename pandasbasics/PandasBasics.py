import pandas as pd
import numpy as np

emp = pd.read_csv(
    "/home/dharani/PycharmProjects/PythonSession/InputFiles/employees", header=None)
emp.columns = ['Id','Name','Age','Gender','Location']

print(emp.tail(2))
