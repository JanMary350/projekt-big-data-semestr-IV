import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv('df_differences.csv')

df1 = df.copy()
df1 = df1.dropna()

df2 = df.copy()
df2 = df2.fillna(df2.median())

"""random forest"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(df1.drop('target', axis=1), df1['target'], test_size=0.3, random_state=42)

rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print("accuracy score for random forest with dropped missing values")
print(accuracy_score(y_test, y_pred))




"""neural network"""
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

print("accuracy score for neural network with dropped missing values")
print(model.evaluate(X_test, y_test)[1])

print("__________________________________________________________________________________________")
print("__________________________________________________________________________________________")
print("__________________________________________________________________________________________")



"""with filled missing values"""
X_train, X_test, y_train, y_test = train_test_split(df2.drop('target', axis=1), df2['target'], test_size=0.3, random_state=42)
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print("accuracy score for random forest with filled missing values by median")
print(accuracy_score(y_test, y_pred))

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

print("accuracy score for neural network with filled missing values by median")
print(model.evaluate(X_test, y_test)[1])


print("__________________________________________________________________________________________")
print("__________________________________________________________________________________________")
print("__________________________________________________________________________________________")
print("benchmark models to randomly picked class")
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

dummy_clf = DummyClassifier(strategy="stratified")
dummy_clf.fit(X_train, y_train)
y_pred = dummy_clf.predict(X_test)
print("accuracy score for dummy classifier")
print(accuracy_score(y_test, y_pred))
