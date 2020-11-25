<h1>fast_wheels</h1>
<br>
<h2>FastAPI, MongoDB, Docker</h2>
<br>

[[License](https://camo.githubusercontent.com/d91ed7ac7abbd5a6102cbe988dd8e9ac21bde0a73d97be7603b891ad08ce3479/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)

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

