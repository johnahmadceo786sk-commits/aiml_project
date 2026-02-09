from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///students.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"


    id = Column(Integer, primary_key=True)
    hours = Column(Float)
    predicted_marks = Column(Float)


Base.metadata.create_all(bind=engine)