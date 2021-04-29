from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False, default="", server_default="")

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"User #{self.id} ({self.username})"

    def __repr__(self):
        return str(self)


