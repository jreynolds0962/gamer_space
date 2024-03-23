from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Developer(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    founded_year = Column(Integer)
    hq_location = Column(String(255))
    website = Column(String(255))
    
    games = relationship("Game", back_populates="developer")

    def __repr__(self):
        return f'Developer: {self.name}'

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    release_year = Column(Integer)
    genre = Column(String(255))
    overall_rating = Column(REAL)
    
    developer_id = Column(Integer, ForeignKey('developers.id'))
    developer = relationship("Developer",
                             foreign_keys=[developer_id],
                             primaryjoin="Game.developer_id == Developer.id"
                             )

    def __repr__(self):
        return f'Game: {self.name}'
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            }