import math

from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from config import MAX_RESULTS


def get_sturbucks_near_me(db: Session, geo, max_dist):
    ## get square area
    # geo is touple of (lat, long)

    ## sqlite not support of cos, sin etc so we get the square results, and we will do more filtering later
    ## when move PgSQL or other advance db, we may consider to cnange the query

    lat_dist = 1.0 / 111.1 * max_dist
    lon_dist = 1.0 / abs(111.1 * math.cos(geo[1])) * max_dist;
    sql = f"""
   SELECT 
    'https://maps.google.com/?q='|| s.latitude ||',' || s.longitude as googlemaps_link,
    s.*
    FROM starbucks s
   WHERE latitude 
   BETWEEN {geo[0] - lat_dist} AND {geo[0] + lat_dist} AND longitude BETWEEN {geo[1] - lon_dist} AND {geo[1] + lon_dist}
    LIMIT {MAX_RESULTS}
    """

    # print(text(sql))
    res = db.execute(text(sql)).all()
    return [i._asdict() for i in res]
