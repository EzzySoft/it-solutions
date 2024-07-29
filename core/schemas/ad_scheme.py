from pydantic import BaseModel


class AdvertisementScheme(BaseModel):
    ad_id: int
    title: str
    author: str
    views: int
    position_number: int
