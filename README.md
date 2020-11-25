<h1>fast_wheels</h1>
<br>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Twitter Follow](https://img.shields.io/twitter/follow/joeDot2?style=social)](https://twitter.com/JoeDot2)

<br>

<h2>FastAPI, MongoDB, Docker</h2>
<br>


1. Clone the repo

        git clone https://github.com/joedots1/fast_wheels.git

2. Build the Docker Containers

        docker-compose up --build

3. Check The API - 0.0.0.0:8000/docs

4. Attach shell to mongodb container:

        docker exec -it mongodb /bin/bash

5. Seed the mongo db

        mongoimport --db admin --collection car_collection -u admin -p - admin --file all_cars.json --jsonArray

6. Open mongo shell

        mongo -u admin -p admin
        use admin 

7. Create text search index on model

        db.car_collection.createIndex({model:"text"})
