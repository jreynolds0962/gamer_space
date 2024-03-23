from sqlalchemy.orm import Session
from . import models, schemas

def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()

def gate_games_by_name(db: Session, name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(models.Game.name == name).offset(skip).limit(limit).all()

def get_games_by_developer(db: Session, developer_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(models.Game.developer_id == developer_id).offset(skip).limit(limit).all()

def create_game(db: Session, game: schemas.VideoGameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_developer_by_id(db: Session, developer_id: int):
    return db.query(models.Developer).filter(models.Developer.id == developer_id).first()

def get_developers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Developer).offset(skip).limit(limit).all()

def create_developer(db: Session, developer: schemas.DeveloperCreate):
    db_developer = models.Developer(**developer.dict())
    db.add(db_developer)
    db.commit()
    db.refresh(db_developer)
    return db_developer
