from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime
from mpt_app.db.base import Base

# 循環参照の回避
if TYPE_CHECKING:
    from .problem import Problem  # noqa: F401

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, unique=True)
    school_year = Column(Integer, index=True)
    problems = relationship("Problem", back_populates="unit")
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
