from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:password@YOUR_RDS_ENDPOINT:5432/studentdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class StudentRecord(Base):
    __tablename__ = "student_records"

    id = Column(Integer, primary_key=True, index=True)
    study_hours = Column(Float)
    attendance = Column(Float)
    previous_marks = Column(Float)
    assignment_score = Column(Float)
    prediction = Column(String)
    probability = Column(Float)

def create_tables():
    Base.metadata.create_all(bind=engine)