weather=['Sunny','Sunny','Overcast','Rainy','Rainy',
         'Rainy','Overcast',
         'Sunny','Sunny',
         'Rainy','Sunny','Overcast',
         'Overcast','Rainy']

temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

'''
you need to convert these string labels into numbers.
for example: 'Overcast', 'Rainy', 'Sunny' as 0, 1, 2.
This is known as label encoding.Scikit - learn provides LabelEncoder library
for encoding labels with a value between 0 and 
one less than the number of discrete classes.
'''

# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)

print ("weather :",weather_encoded)
# Converting string labels into numbers
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print ("Temp:",temp_encoded)
print ("Play:",label)

features=list(zip(weather_encoded,temp_encoded))
print (features)

# Generating Model
# -Generate a model using naive bayes classifier in the following steps:
#     Create naive bayes classifier
#     Fit the dataset on classifier
#     Perform prediction


from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print ("Predicted Value:", predicted)

