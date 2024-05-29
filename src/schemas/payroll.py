from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional
from datetime import date

##########################################################################
class Payroll(BaseModel):
    id: int = Field(title="Id of the payroll")
    date_: str = Field(title="date of the payroll")
    activity: str = Field(min_length=4, max_length=100, title="activity of the payroll")
    category: str = Field(min_length=4, max_length=50, title="Category of the payroll")
    responsible: str = Field(min_length=4, max_length=50, title="Responsible of the payroll")
    observation: Optional[str] = Field(default=None,min_length=4, max_length=100, title="Observation of the payroll")

    class Config:
        json_schema_extra = {
            "example": {
            "id": 1,
            "date_": "2024-03-13",
            "activity": "Siembra de café",
            "category": "Café",
            "responsible": "Oscar Alzate",
            "observation": "Ninguna"
        }
    }
