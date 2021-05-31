from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class Section(Base):
    __tablename__ = 'sections'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    title = Column(String(120), unique=True, nullable=False, default="", server_default="")

    sections = relationship("Post", back_populates="section")

    def __str__(self):
        return f"Section #{self.id} ({self.title})"

    def __repr__(self):
        return str(self)
