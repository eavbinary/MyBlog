from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base
from post import Post


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, default="", server_default="")
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    post = relationship(Post, back_populates="tags")

    def __str__(self):
        return f"Tag #{self.id} ({self.name})"

    def __repr__(self):
        return str(self)
