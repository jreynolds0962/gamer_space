from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Developer(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    founded_year = Column(Integer)
    hq_location = Column(String(255))
    website = Column(String(255))
    

    def __repr__(self):
        return f'Developer: {self.name}'

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    release_year = Column(Integer)
    genre = Column(String(255))
    overall_rating = Column(Float)
    developer = Column(Integer, ForeignKey('developers.id'))
      

    def __repr__(self):
        return f'Game: {self.name}'
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre
            }