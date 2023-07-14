from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from mpt_app.db import Base

if TYPE_CHECKING:
    from mpt_app.models.chapter import Chapter # noqa: F401

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    statement = Column(String(512))
    is_solved = Column(Boolean, default=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    chapter = relationship("Chapter", back_populates="problems")
