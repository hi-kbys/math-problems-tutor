from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from mpt_app.db import Base

if TYPE_CHECKING:
    from mpt_app.models.problem import Problem  # noqa: F401

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1024), index=True)
    school_year = Column(Integer, index=True)
    problems = relationship("Problem", back_populates="chapter")
