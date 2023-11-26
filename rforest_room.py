import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import operator
#As only square meters and price have impactful correlation with number of rooms, only they will be used for room_number prediction

df = pd.read_excel('Processed data 26.11.2023..xlsx')
df['room_groups'] = df['room_number'].apply(lambda x: '<2.5' if x < 2.5 else ('<4.5' if x < 4.5 else '4.5+'))
print(df)
values = df[['price', 'sq_meters']].values.tolist()
labels = list(df['room_groups'])
train_values, test_values, train_labels, test_labels = train_test_split(values, labels, test_size=0.25)
scaler = StandardScaler()
train_values_scaled = scaler.fit_transform(train_values)
test_values_scaled = scaler.fit_transform(test_values)


accuracies = []
index = list(range(100, 1500, 100))
for i in range(100, 1500, 100):
    classifier = RandomForestClassifier(n_estimators=1500)
    classifier.fit(train_values_scaled, train_labels)

    acc = classifier.score(test_values_scaled, test_labels)
    print(acc)
    accuracies.append(acc)

result = dict(zip(index, accuracies))
print(max(result.items(), key=operator.itemgetter(1)))
