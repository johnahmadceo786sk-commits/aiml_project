from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_performance
from database import SessionLocal, StudentRecord, create_tables

app = FastAPI()

create_tables()

class StudentInput(BaseModel):
    study_hours: float
    attendance: float
    previous_marks: float
    assignment_score: float

@app.post("/predict")
def predict(data: StudentInput):
    features = [
        data.study_hours,
        data.attendance,
        data.previous_marks,
        data.assignment_score
    ]

    result, prob = predict_performance(features)

    db = SessionLocal()
    record = StudentRecord(
        study_hours=data.study_hours,
        attendance=data.attendance,
        previous_marks=data.previous_marks,
        assignment_score=data.assignment_score,
        prediction="Pass" if result == 1 else "Fail",
        probability=prob
    )

    db.add(record)
    db.commit()
    db.close()

    return {
        "prediction": "Pass" if result == 1 else "Fail",
        "probability": prob
    }