from pydantic import BaseModel
from datetime import date

class SalesCreate(BaseModel):
    date: date
    quantity: int
    price: float

class SalesRead(SalesCreate):
    id: int