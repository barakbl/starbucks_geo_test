from pydantic import BaseModel


class Adress(BaseModel):
    city: str
    state: str
    street: str
    street_no: int


class Branch(BaseModel):
    id: str
    starbucks_id: str
    name: str
    store_name: str
    phone_number: str
    street1: str
    street2: str
    street3: str
    city: str
    postal_code: str
    longitude: float
    latitude: float
    googlemaps_link: str
    distance: float
