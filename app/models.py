from typing import Optional

from pydantic import BaseModel, Field


class CarSchema(BaseModel):
    toy_num: str = Field(...)
    col_num: str = Field(...)
    model: str = Field(...)
    series: str = Field(...)
    series_num: str = Field(...)
    photo_url: str = Field(...)
    year: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "toy_num": "GHC01",
                "col_num": "088",
                "model": "Aston Martin Vulcan",
                "series": "Factory Fresh",
                "series_num": "6/10",
                "photo_url": "https://hotwheels.fandom.com/wiki/List_of_2020_Hot_Wheels?file=Aston_Martin_Vulcan.jpg",
                "year": 2020,
            }
        }


class UpdateCarModel(BaseModel):
    toy_num: Optional[str]
    col_num: Optional[str]
    model: Optional[str]
    series: Optional[str]
    series_num: Optional[str]
    photo_url: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "toy_num": "GHC01",
                "col_num": "088",
                "model": "Aston Martin Vulcan",
                "series": "Factory Fresh",
                "series_num": "6/10",
                "photo_url": "https://hotwheels.fandom.com/wiki/List_of_2020_Hot_Wheels?file=Aston_Martin_Vulcan.jpg",
                "year": 2020,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
