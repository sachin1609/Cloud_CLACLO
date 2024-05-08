from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class University(Base):
    __tablename__ = "universities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    activation_date = Column(Date)
    deactivation_date = Column(Date)
    surveys = relationship("Survey", back_populates="university")

class Survey(Base):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True, index=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    university = relationship("University", back_populates="surveys")
    survey_type = Column(String, index=True)  # "student" or "staff"
    conducted_on = Column(Date)
    data = Column(Text)  # JSON or any serialized format

class SurveyReport(Base):
    __tablename__ = "survey_reports"
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    survey = relationship("Survey")
    detailed_report = Column(Text)  # JSON or any serialized format containing detailed statistical analysis

