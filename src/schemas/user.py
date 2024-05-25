from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

##########################################################################
class User (BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the user")
    user: str = Field(min_length=4, max_length=50, title="Name of the user")
    password: str = Field(min_length=4, max_length=50, title="Name of the user")
    name: str = Field(min_length=4, max_length=50, title="Name of the user")
    email: str = Field(min_length=4, max_length=50, title="Name of the user")
    rol: str = Field(min_length=4, max_length=50, title="Name of the user")

    @validator("name")
    @classmethod
    def validate_no_poison(cls, value):
        if value == "poison":
            raise ValueError("Posion should not be expended as user")
        return value

    @model_validator(mode='after')
    def validate_expensive_cheap_users(self):
        if self.name == "cheap" and self.price > 100000:
            raise ValueError("A user with that price cannot be named cheap.")
        return self

    class Config:
        json_schema_extra = {
            "example": {
            "id": 1,
            "user": "oscar ",
            "password": "hola123",
            "name": "Oscar Alzate",
            "email": "none",
            "rol":"admin"
        }
    }
