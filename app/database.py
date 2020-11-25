import os
from dotenv import load_dotenv

import motor.motor_asyncio
from bson.objectid import ObjectId

load_dotenv()
USER = os.getenv("MONGO_USER")
PASS = os.getenv("MONGO_PW")
DB = os.getenv("MONGO_DEF_DB")
PORT = os.getenv("MONGO_PORT")
MONGO_DETAILS = f"mongodb://{USER}:{PASS}@mongodb:{PORT}/{DB}"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['admin']

car_collection = database.get_collection("car_collection")


# helpers
def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "toy_num": car["toy_num"],
        "col_num": car["col_num"],
        "model": car["model"],
        "series": car["series"],
        "series_num": car["series_num"],
        "photo_url": car["photo_url"],
        "year": car["year"],
    }


# async crud ops for our cars

# Retrieve all cars present in the database
async def retrieve_cars():
    cars = []
    async for car in car_collection.find():
        cars.append(car_helper(car))
    return cars


# Add a new car into to the database
async def add_car(car_data: dict) -> dict:
    car = await car_collection.insert_one(car_data)
    new_car = await car_collection.find_one({"_id": car.inserted_id})
    return car_helper(new_car)


# Retrieve a car with a matching ID
async def retrieve_car(id: str) -> dict:
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        return car_helper(car)


# Update a car with a matching ID
async def update_car(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        updated_car = await car_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_car:
            return True
        return False


# Delete a car from the database
async def delete_car(id: str):
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        await car_collection.delete_one({"_id": ObjectId(id)})
        return True

# search cars by model
async def car_model_search(model: str) -> dict:
    cars = []
    async for car in car_collection.find({"$text": {"$search": model}}).sort([('score', {'$meta': 'textScore'})]):
        cars.append(car_helper(car))
    return cars


# get all cars in a series
async def retrieve_series(series: str) -> dict:
    cars = []
    async for car in car_collection.find({"series":series}):
        cars.append(car_helper(car))
    return cars


# get all cars run in a given year
async def retrieve_year(year: int) -> dict:
    cars = []
    async for car in car_collection.find({"year":year}):
        cars.append(car_helper(car))
    return cars