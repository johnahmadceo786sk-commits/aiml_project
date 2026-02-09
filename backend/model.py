import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


# Train model

def train_model():
    df = pd.read_csv("data.csv")
    X = df[["hours"]]
    y = df["marks"]


    model = LinearRegression()
    model.fit(X, y)


    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)




# Load model


def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)