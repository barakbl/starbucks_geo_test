# sturbucks finder

This is a FastAPI based REST API service that find a starbucks branches near a given place

sql_app.db is a db of branches loaded using the resoueces/import_csv.py script and stores.csv as the db source
 

## INSTALL
create venv:
```
python3 -m venv venv
```
activate the virtual env:
```
source venv/bin/activate 
```

install deps: 
```
pip install -r requirements.txt
```

## Usage

run the service (debug/local mode)
```
python main.py
```

## usage: 

access rest api swagger: http://127.0.0.1:8888/docs


## TODO:

1. Add python logger
2. Dockerize
3. Tests
4. Install guide for servers
5. change to async is possible for better performance
6. Poetry

