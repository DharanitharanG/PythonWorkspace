import pandas as pd
import numpy as np
import pprint
import decisiontree.BuildDecisionTreeWithPython as bdt
from decisiontree.ConvertDictionaryToGraph import draw_the_graph

input_path ="/home/dharani/PycharmProjects/PythonSession/InputFiles/tennis.csv"
play_tennis_data = pd.read_csv(input_path,header=0)


'''
print(play_tennis_data.keys())
last_col = play_tennis_data.keys()[-1]
print('last_column : ',last_col) #gives last value in list
all_remaining_last_col = play_tennis_data.keys()[:-1]
print('all columns except last column : ',all_remaining_last_col)
print('unique values : ',play_tennis_data[last_col].unique())
print('value counts: ',play_tennis_data[last_col].value_counts())
print('value counts - values : ',play_tennis_data[last_col].value_counts()['Yes'])
print('unique values withCounts: ',np.unique(play_tennis_data[last_col],return_counts=True))
eps = np.finfo(float).eps
print('eps is : ',eps)

overall_entropy = bdt.find_entropy_of_set(play_tennis_data)
print('overall entropy of data : ', overall_entropy)
total_entropy_Outlook = bdt.find_total_entropy_of_attribute(play_tennis_data,'Outlook')
print('entropy of Outlook : ',total_entropy_Outlook)
print('Information Gain for Outlook : ', overall_entropy - total_entropy_Outlook)
total_entropy_Windy = bdt.find_total_entropy_of_attribute(play_tennis_data,'Windy')
print('entropy of Windy : ',total_entropy_Windy)
print('Information Gain for Windy : ', overall_entropy - total_entropy_Windy)
max_information_gain_attribute = bdt.find_max_information_gain_attribute(play_tennis_data)
print(" The Max Information gain attribute is : ", max_information_gain_attribute)

decision_tree = bdt.build_decision_tree(play_tennis_data)
print("\n **************** DECISION TREE ********************* \n")
pprint.pprint(decision_tree)

data = {'Outlook':'Rainy','Humidity':'High','Windy':'Strong'}
to_predict = pd.Series(data)
predicted_value = bdt.predict_the_values(to_predict,decision_tree)

print("\n **************************************************** \n")
print(' The predicted value for : ', data ,' is : ',predicted_value)

draw_the_graph(decision_tree,'/home/dharani/Desktop/play_tennis.png')
'''