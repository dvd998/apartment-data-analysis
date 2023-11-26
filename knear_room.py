import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import operator
# from sklearn.preprocessing import StandardScaler


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
index = []
for i in range(25, 150):
    classifier = KNeighborsClassifier(n_neighbors= i)
    classifier.fit(train_values_scaled, train_labels)

    accuracy = classifier.score(test_values_scaled, test_labels)
    accuracies.append(accuracy)
    index.append(i)
    print(f"Accuracy: {accuracy}")

result = dict(zip(index, accuracies))
print(max(result.items(), key=operator.itemgetter(1)))