import numpy as np
import pandas as pd
# from pandas_profiling import ProfileReport
# Load data
data=pd.read_csv('HR_comma_sep.csv')
print(data.info())
print(data.head())


# Import LabelEncoder (for encoding specific part)
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
data['salary']=le.fit_transform(data['salary'])
data['sales']=le.fit_transform(data['sales'])

save_encoded=data.to_csv("encoded.csv")


# Report=ProfileReport(data)
# Report.to_file("report.html")
# save=data.to_csv("dsdf.csv")


# Spliting data into Feature and

X=data[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'sales', 'salary']]
y=data['left']


# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,stratify=y, random_state=42)  # 70% training and 30% test

# Import MLPClassifer 
from sklearn.neural_network import MLPClassifier

# Create model object
clf = MLPClassifier(hidden_layer_sizes=(6,5),
                    random_state=5,
                    verbose=True,
                    learning_rate_init=0.01)

# Fit data onto the model
clf.fit(X_train,y_train)

# Make prediction on test dataset
ypred=clf.predict(X_test)

import matplotlib.pyplot as plt
# plt.plot(y_test,ypred)
# plt.show()
# Import accuracy score 
from sklearn.metrics import accuracy_score

# Calcuate accuracy
print(accuracy_score(y_test,ypred))
print(ypred)


from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(y_test, ypred)
print(confusion_matrix)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()
