from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Query

from app.database import (
    add_car,
    car_model_search,
    delete_car,
    retrieve_car,
    retrieve_cars,
    update_car,
    car_model_search,
    retrieve_series,
    retrieve_year,
)
from app.models import ErrorResponseModel, ResponseModel, CarSchema, UpdateCarModel

router = APIRouter()


@router.post("/", response_description="car data added into the database")
async def add_car_data(car: CarSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseModel(new_car, "car added successfully.")


@router.get("/", response_description="car retrieved")
async def get_cars():
    cars = await retrieve_cars()
    if cars:
        return ResponseModel(cars, "car data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


@router.get("/{id}", response_description="car data retrieved")
async def get_car_data(id):
    car = await retrieve_car(id)
    if car:
        return ResponseModel(car, "car data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "car doesn't exist.")


@router.delete("/{id}", response_description="car data deleted from the database")
async def delete_car_data(id: str):
    deleted_car = await delete_car(id)
    if deleted_car:
        return ResponseModel(
            "car with ID: {} removed".format(id), "car deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "car with id {0} doesn't exist".format(id)
    )


@router.put("/{id}")
async def update_car_data(id: str, req: UpdateCarModel = Body(...)):
    req = {key: val for key, val in req.dict().items() if val is not None}
    updated_car = await update_car(id, req)
    if updated_car:
        return ResponseModel(
            "car with ID: {} name update is successful".format(id),
            "car updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


# text search of models
@router.get("/model/{model}", response_description="text search of models")
async def search_models(model):
    cars = await car_model_search(model)
    if cars:
        return ResponseModel(cars, "car data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


# list series names
@router.get("/series/{series}", response_description="all series names")
async def get_series(series):
    cars = await retrieve_series(series)
    if cars:
        return ResponseModel(cars, "series data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


# get all cars run in a given year
@router.get("/year/{year}", response_description="all cars in a given year")
async def get_year_cars(year):
    cars = await retrieve_year(year)
    if cars:
        return ResponseModel(cars, "series data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


# search for -specific- model of car
# @router.get("/model/{query}", response_description="car by model name")
# async def model_name(query):
#     car = await get_car_by_model(query)
#     if car:
#         return ResponseModel(car, "car data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "car doesn't exist.")
