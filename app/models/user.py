from sqlalchemy import Integer, String, Column

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), index=True, nullable=True)
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String(256), nullable=True)
    phone = Column(String(256), nullable=True)
