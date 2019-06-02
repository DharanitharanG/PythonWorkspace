from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy as np

df = pd.read_csv('/home/dharani/PycharmProjects/PythonSession/InputFiles/tennis.csv',header=0)

lb = LabelEncoder()
df['outlook_'] = lb.fit_transform(df['Outlook'])
df['humidity_'] = lb.fit_transform(df['Humidity'] )
df['windy_'] = lb.fit_transform(df['Windy'] )
df['play_'] = lb.fit_transform(df['PlayTennis'] )
# df['orig_outlook']=lb.inverse_transform(lb.fit_transform(df['Outlook']))
print(df.head())

X = df.iloc[:,4:7]
Y = df.iloc[:,7]

X_train, X_test , y_train,y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
print(X_test)
clf_entropy = DecisionTreeClassifier(criterion='entropy')
clf_entropy.fit(X,Y)
print('x-test ', X_test)
print('y test : \n ', y_test)
y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

print("Accuracy is :{0}".format(accuracy_score(y_test.astype(int),y_pred_en) * 100))

#
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf_entropy, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = X.keys(),class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('/home/dharani/Desktop/play_tennis.png')
Image(graph.create_png())





