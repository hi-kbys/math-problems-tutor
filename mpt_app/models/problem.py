from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    ForeignKey, 
    Boolean,
    DateTime
    )

from sqlalchemy.orm import relationship

from datetime import datetime
from mpt_app.db.base import Base

# 循環参照の回避
if TYPE_CHECKING:
    from .unit import Unit # noqa: F401

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    statement = Column(String(512))
    is_solved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"))
    unit = relationship("Unit", back_populates="problems")
