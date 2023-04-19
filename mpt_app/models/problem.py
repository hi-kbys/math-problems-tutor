from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mpt_app.db import Base

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1024))
    statement = Column(String(1024))
    is_solved = Column(String(1024))
