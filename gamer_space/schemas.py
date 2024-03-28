from pydantic import BaseModel, Field
from typing import Optional


class VideoGameBase(BaseModel):
    name: str
    release_year: int
    genre: Optional[str]
    overall_rating: Optional[float]

class DeveloperBase(BaseModel):
    name: str
    founded_year: Optional[int]
    hq_location: Optional[str]
    website: Optional[str]





class VideoGameCreate(VideoGameBase):
    developer: str

class DeveloperCreate(DeveloperBase):
    pass




class VideoGame(VideoGameBase):
    id: int
    developer_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Super Mario Bros",
                "release_date": 1985,
                "genre": "Platformer",
                "overall_rating": 4.5
                # "developer_id": 1
            }
        }

class Developer(DeveloperBase):
    id: int
    # games: list[VideoGame] = Field(include={"name"})

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Nintendo",
                "founded_year": 1889,
                "headquarters": "Kyoto, Japan",
                "website": "https://www.nintendo.com/"
                # "games": []
            }
        }