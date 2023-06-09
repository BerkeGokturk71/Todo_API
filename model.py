from database import Base
from sqlalchemy import String,Boolean,VARCHAR,Integer,Column,ForeignKey,Text,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__="user"

    id = Column(Integer,primary_key=True)
    username =Column(String,unique=True)
    email = Column(String,unique=True,nullable=False)
    password =Column(String,nullable=False)
    is_staff = Column(Boolean,default=False)
    todo = relationship("ToDo",back_populates="user")


class ToDo(Base):
    __tablename__="todo"
    id = Column(Integer,primary_key=True)
    topic = Column(VARCHAR(50),nullable=False,unique=True)
    text =Column(VARCHAR(255),nullable=False)
    todo_id = Column(Integer,ForeignKey("user.id"))
    date = Column(DateTime,default=datetime.utcnow)

