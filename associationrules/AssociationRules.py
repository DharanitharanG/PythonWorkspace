
'''
employees = pd.read_csv('/home/dharani/Downloads/employees.csv',
                         header=None)
print(employees)

employeesList= []
for i in range(0,4):
    employeesList.append([str(employees.values[i,j]) for j in range (0,3)])

print(employeesList)
'''
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('/home/dharani/Downloads/store_data.csv',
                         header=None)
sample = store_data.head()
print(sample)


records = []
for i in range(0, 7501):
        records.append([str(store_data.values[i,j])for j in range(0, 20)])
association_rules = apriori(records,min_support=0.0133,
                            min_confidence=0.3,min_lift=3,min_length=2)
association_results = list(association_rules)
print('len(association_results)) : ',len(association_results))
print(association_results[0])
print("----------------------------------------------------------")
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]));print("Confidence: " + str(item[2][0][2]));
    print("Lift: " + str(item[2][0][3]));print("===================")




