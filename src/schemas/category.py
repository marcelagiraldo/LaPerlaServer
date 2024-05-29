from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional
from datetime import date

##########################################################################
class Category (BaseModel):
    id: int = Field(title="Id of the Category")
    name: str = Field(min_length=4, max_length=50, title="Category of the Category")

    class Config:
        json_schema_extra = {
            "example": {
            "id": 1,
            "name": "None",
        }
    }
