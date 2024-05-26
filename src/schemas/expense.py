from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional
from datetime import date

##########################################################################
class Expense (BaseModel):
    id: int = Field(title="Id of the expense")
    date_: str = Field(title="Expiration date of the expense")
    category: str = Field(min_length=4, max_length=50, title="Category of the expense")
    price: float = Field(default="1000", le=5000000, lg=100, title="Price of the expense")
    desciption: str = Field(min_length=4, max_length=50, title="Description of the expense")
    observation: Optional[str] = Field(default=None,min_length=4, max_length=50, title="Observation of the expense")

    class Config:
        json_schema_extra = {
            "example": {
            "id": 1,
            "date_": "2024-06-13",
            "category": "Café",
            "price": "30000",
            "desciption": "Compra de abono",
            "observation":""
        }
    }
