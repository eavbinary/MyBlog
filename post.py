from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

from base import Base
from section import Section
from user import User


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)

    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    title = Column(String(120), nullable=False, default="", server_default="")
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    user = relationship(User, back_populates="posts")
    section = relationship(Section, back_populates="sections")
    tags = relationship("Tag", back_populates="post")

    def __str__(self):
        return f"Post #{self.id} ({self.title})"

    def __repr__(self):
        return str(self)
