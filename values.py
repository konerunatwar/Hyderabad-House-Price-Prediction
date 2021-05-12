from pydantic import BaseModel

class value(BaseModel):
    property_size: int
    bhk: int
    Gymnasium: int
    SwimmingPool: int
    LiftAvailable: int
    locality: str
