from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from Model.BaseModel import BaseModel


class Comment(BaseModel):
    __tablename__ = 'comments'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    text = Column(Text, nullable=False)

    user = relationship('User', foreign_keys=[user_id])
