from sqlalchemy import Column, Integer, String
from app.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    additional_info = Column(String, nullable=True)
