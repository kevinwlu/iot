# Pedestrian and bicyclist counts on campus
# https://catalog.data.gov/dataset/traffic-data
# Class dates by Support Vector Classifier (SVC)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

FTD = pd.read_csv("pedestrian-and-bicyclist-counts.csv")

X = FTD.drop(['Date','Class'], axis=1)
y = FTD['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
