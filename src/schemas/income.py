from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

##########################################################################
class Income (BaseModel):
    id: int = Field(title="Id of the income")
    date_: str = Field(title="Expiration date of the product")
    category: str = Field(min_length=4, max_length=50, title="Category of the income")
    price: float = Field(default="1000", le=5000000, lg=100, title="Price of the product")
    description: str = Field(min_length=4, max_length=50, title="Description of the income")
    observation: Optional[str] = Field(default=None,min_length=4, max_length=50, title="Observation of the income")

    class Config:
        json_schema_extra = {
            "example": {
            "id": 1,
            "date_": "2023-06-12",
            "category": "Café",
            "price": "500",
            "description": "Café pergamino seco",
        }
    }
