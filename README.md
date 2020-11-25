<h1>fast_wheels</h1>
<br>
<h2>FastAPI, MongoDB, Docker</h2>
<br>


1. Pull 
2. docker-compose up --build 
3. check 127.0.0.1:8000/docs 
4. attach shell to mongodb container
5. seed the mongo db
    - mongoimport --db admin --collection car_collection -u admin -p - admin --file all_cars.json --jsonArray
6. open mongo shell
    - mongo -u admin -p admin
    - use admin 
7. create text search index on model 
    - db.car_collection.createIndex({model:"text"})

