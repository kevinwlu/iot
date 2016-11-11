import numpy as np
from pandas import *
options.mode.chained_assignment = None
data=read_csv('train.csv')
columns=data.columns
look_up=(data.groupby(['Sex', 'Pclass']).Survived.mean())
test=read_csv('test.csv')
test['Prediction']=0
for i in range(len(test)):
    test.Prediction[i]=round(look_up[test.Sex[i]][test.Pclass[i]])
test.to_csv('result.csv', index=False)
data['Fare_Bracket']=0
test['Fare_Bracket']=0
na=sum(test.Fare != test.Fare)
wh_badfare=np.flatnonzero(test.Fare != test.Fare)
sv = test.Fare[test.Fare != test.Fare]
test.Fare[test.Fare != test.Fare]=(3-test.Pclass)*11
test.Fare_Bracket=np.array([min(int(price/10),3) for price in test.Fare])
test.Fare[wh_badfare]=sv
data.Fare_Bracket=np.array([min(int(price/10),3) for price in data.Fare])
look_up2=(data.groupby(['Sex', 'Pclass', 'Fare_Bracket']).Survived.mean())
for i in range(len(test)):
    test.Prediction[i] = round(look_up2[test.Sex[i]][test.Pclass[i]][test.Fare_Bracket[i]])
test.to_csv('result2.csv', index=False)
print('Survived:')
print(look_up)
print('Number of Missing Fare: %d' % (na))
print('Indices of Missing Fare: %d' % (wh_badfare))
print('Survived:')
print(look_up2)
