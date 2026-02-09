from fastapi import FastAPI
from pydantic import BaseModel
from model import train_model, load_model
from database import SessionLocal, Prediction


app = FastAPI()


train_model()
model = load_model()


class Input(BaseModel):
    hours: float


@app.post("/predict")
def predict(data: Input):
    prediction = model.predict([[data.hours]])[0]


    db = SessionLocal()
    record = Prediction(hours=data.hours, predicted_marks=prediction)
    db.add(record)
    db.commit()


    return {"predicted_marks": round(prediction, 2)}