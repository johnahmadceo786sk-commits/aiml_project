import numpy as np
from sklearn.linear_model import LogisticRegression

# Dummy training data
X = np.array([
    [5, 80, 70, 60],
    [1, 40, 35, 30],
    [6, 90, 85, 75],
    [2, 50, 45, 40],
    [7, 95, 92, 88]
])

y = np.array([1, 0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

def predict_performance(features):
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]
    probability = model.predict_proba(features_array)[0][1]

    return int(prediction), float(probability)