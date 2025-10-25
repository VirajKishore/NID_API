from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    body = Column(String)
    last_updated = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Note(id={self.id}, title={self.title}, body={self.body}, last_updated={self.last_updated})"