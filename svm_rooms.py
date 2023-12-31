import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('Processed data 26.11.2023..xlsx')
df['room_groups'] = df['room_number'].apply(lambda x: '<2.5' if x < 2.5 else ('<4.5' if x < 4.5 else '4.5+'))
print(df)
values = df[['price', 'sq_meters']].values.tolist()
labels = list(df['room_groups'])
train_values, test_values, train_labels, test_labels = train_test_split(values, labels, test_size=0.25)
scaler = StandardScaler()
train_values_scaled = scaler.fit_transform(train_values)
test_values_scaled = scaler.fit_transform(test_values)

train_values, test_values, train_labels, test_labels = train_test_split(values, labels, train_size= 0.8, test_size=0.2, random_state=100)

classifier = SVC(gamma=0.01, kernel='rbf', C = 0.5)
classifier.fit(train_values, train_labels)

print(classifier.score(test_values, test_labels))