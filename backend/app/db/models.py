from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(Text)
    skills = Column(Text)
    experience = Column(String)
    education = Column(String)
    responsibilities = Column(Text)

    candidates = relationship("Candidate", back_populates="job")

class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    skills = Column(Text)
    experience = Column(Text)
    education = Column(Text)
    certifications = Column(Text)
    match_score = Column(Float)
    explanation = Column(Text)
    shortlisted = Column(Boolean, default=False)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship("Job", back_populates="candidates")
