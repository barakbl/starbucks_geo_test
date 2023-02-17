from typing import List

import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

import config
import crud
import schemas
from database import SessionLocal
from geo import get_geo, get_dist_between_2_points

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_starbucks_near_address(address: str, max_dist: float, db: Session) -> List[schemas.Branch]:
    input_geo = get_geo(address)
    lst = crud.get_sturbucks_near_me(db, input_geo, max_dist)
    if not lst:
        return []

    ## we filter the list, as from db we got rectangle, but actually we need to get by circle
    filtered_lst = []
    for idx, item in enumerate(lst):
        dist = get_dist_between_2_points(input_geo, (item['latitude'], item['longitude']))
        item["distance"] = dist
        if dist <= config.MAX_DIST:
            filtered_lst.append(item)

    ## sort the result start from nearest places
    ordered_lst = sorted(filtered_lst, key=lambda d: d['distance'])
    return ordered_lst


@app.get("/", response_class=HTMLResponse)
def homepage():
    return """

     <a href="http://localhost:8888/docs">API (Swagger)</a> <br>"
    """


@app.get("/api/v1/starbucks/near/{address}", response_model=List[schemas.Branch])
def near_ctrl(address: str, db: Session = Depends(get_db)):
    max_dist = config.MAX_DIST
    lst = get_starbucks_near_address(address, max_dist, db)
    return lst


if __name__ == '__main__':
    uvicorn.run("main:app", host=config.SERVER_IP, port=config.SERVER_PORT, reload=config.SERVER_RELOAD)
