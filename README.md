<h1>fast_wheels</h1>
<br>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fimg.shields.io%2Ftwitter%2Furl%3Fstyle%3Dsocial%26url%3Dhttps%253A%252F%252Fgithub.com%252Fjoedots1%252Ffast_wheels)
<br>

<h2>FastAPI, MongoDB, Docker</h2>
<br>

1. git clone https://github.com/joedots1/fast_wheels.git
2. docker-compose up --build 
3. check 127.0.0.1:8000/docs 
4. attach shell to mongodb container
    - $ docker exec -it mongodb /bin/bash
5. seed the mongo db
    - $ mongoimport --db admin --collection car_collection -u admin -p - admin --file all_cars.json --jsonArray
6. open mongo shell
    - $> mongo -u admin -p admin
    - $> use admin 
7. create text search index on model 
    - $> db.car_collection.createIndex({model:"text"})
