from sqlalchemy import Column, Text, DECIMAL, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from Model.BaseModel import BaseModel

class Task(BaseModel):
    __tablename__ = 'tasks'

    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(Text, nullable=False)
    date_complited = Column(DateTime)

    user = relationship('User', foreign_keys=[user_id])