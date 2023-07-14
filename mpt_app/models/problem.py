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
    from .chapter import Chapter # noqa: F401

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    statement = Column(String(512))
    is_solved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    chapter = relationship("Chapter", back_populates="problems")


# class Chapter(Base):
#     __tablename__ = "chapters"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100), index=True, unique=True)
#     school_year = Column(Integer, index=True)
#     problems = relationship("Problem", back_populates="chapter")
#     created_at = Column(DateTime, default=datetime.now(), nullable=False)
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
