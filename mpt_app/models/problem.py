from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mpt_app.db import Base

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    statement = Column(String)
    is_solved = Column(String)
