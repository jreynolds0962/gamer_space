from pydantic import BaseModel
from typing import Optional


class VideoGameBase(BaseModel):
    name: str
    release_year: int
    genre: Optional[str]
    overall_rating: Optional[float]

class VideoGameCreate(VideoGameBase):
    pass

class VideoGame(VideoGameBase):
    id: int
    developer: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Super Mario Bros",
                "release_date": 1985,
                "genre": "Platformer",
                "overall_rating": 4.5
            }
        }

class DeveloperBase(BaseModel):
    name: str
    founded_year: Optional[int]
    hq_location: Optional[str]
    website: Optional[str]

class DeveloperCreate(DeveloperBase):
    pass

class Developer(DeveloperBase):
    id: int
    games: list[VideoGame] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Nintendo",
                "founded_year": 1889,
                "headquarters": "Kyoto, Japan",
                "website": "https://www.nintendo.com/"
            }
        }