import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

# Train model
def train_model():
    df = pd.read_csv(DATA_PATH)
    X = df[["hours"]]
    y = df["marks"]

    model = LinearRegression()
    model.fit(X, y)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

# Load model
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)
