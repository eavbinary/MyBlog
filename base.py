from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = 'my_blog.db'

engine = create_engine(f"sqlite:///{DB_NAME}", echo=False)
Base = declarative_base(bind=engine)
