from fastapi import HTTPException
from geopy.geocoders import Nominatim
from haversine import haversine


def get_dist_between_2_points(geo1: tuple, geo2: tuple) -> float:
    '''
    This function find the distance between to geo lpcaction using haversine algorithm

    :param geo1: touple of geo location
    :param geo2: touple of geo location of second location

    :return: a float represent the distance in KM
    '''
    dist = haversine(geo1, geo2)
    return round(dist,2)


def get_geo(address: str) -> tuple:
    '''
    This function find the geolocation of a given adress

    :param address: an adress to find geo for
    :return: a tuple of latitude and longtitude
    '''

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(address)
    if getLoc is None:
        raise HTTPException(status_code=404, detail="Given address not found")
    print(f" the geo located address for {address} is: {getLoc.address}")
    return (getLoc.latitude, getLoc.longitude)
