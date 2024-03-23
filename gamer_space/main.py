from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home_page():
    return {"message": "Welcome to Gamer Space!"}

@app.post("/developers/", response_model=schemas.Developer, tags=["developers"])
def create_developer(developer: schemas.DeveloperCreate, db: Session = Depends(get_db)):
    return crud.create_developer(db=db, developer=developer)

@app.get("/developers/", response_model=list[schemas.Developer], tags=["developers"])
def read_developers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    developers = crud.get_developers(db, skip=skip, limit=limit)
    if developers is None:
        raise HTTPException(status_code=404, detail="No developers found")
    return developers

@app.get("/developers/{developer_id}", response_model=schemas.Developer, tags=["developers"])
def read_developer(developer_id: int, db: Session = Depends(get_db)):
    db_developer = crud.get_developer_by_id(db, developer_id=developer_id)
    if db_developer is None:
        raise HTTPException(status_code=404, detail="Developer not found by given ID")
    return db_developer

@app.post("/games/", response_model=schemas.VideoGame, tags=["games"])
def create_game(game: schemas.VideoGameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)

@app.get("/games/", response_model=list[schemas.VideoGame], tags=["games"])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games

@app.get("/games/{game_id}", response_model=schemas.VideoGame, tags=["games"])
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game_by_id(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found by given ID")
    return db_game