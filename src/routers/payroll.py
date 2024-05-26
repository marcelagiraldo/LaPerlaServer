from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.payroll import Payroll

payroll_router = APIRouter()

payrolls = [
    {
        "id": 1,
        "date_": "2024-03-13",
        "activity": "Siembra de café",
        "category": "Café",
        "responsible": "Oscar Alzate"
    },
    {
        "id": 2,
        "date_": "2024-05-15",
        "activity": "Abona de café",
        "category": "Café",
        "responsible": "Oscar Alzate",
        "observation": "Faltó por abonar"
    }
]

#-----------------CRUD------------------------
@payroll_router.get('/payrolls',
tags=['payrolls'],
response_model=List[Payroll],
description="Returns all payrolls stored")
def get_all_payrolls() -> List[Payroll]:
    result = []
    for element in payrolls:
        result.append(element)
    return JSONResponse(content=result, status_code=200)

@payroll_router.get('/payrolls/{id}',tags=['payrolls'],response_model=Payroll,
description="Returns data of one specific payroll")
def get_payroll(id: int = Path(ge=1, le=5000)) -> Payroll:
    for element in payrolls:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content=None, status_code=404)

@payroll_router.post('/payrolls',
          tags=['payrolls'],
          response_model=dict,
          description="Creates a new payroll")
def create_product(payroll: Payroll = Body()) -> dict:
    payrolls.append(payroll.model_dump())
    return JSONResponse(content={
        "message": "The product was created successfully",
        "data": payroll.model_dump()
    }, status_code=201)

@payroll_router.put('/payrolls/{id}',tags=['payrolls'],response_model=dict,description="Updates the data of specific payroll")
def update_payroll(id: int = Path(ge=1),payroll: Payroll = Body()) -> dict:
    for element in payrolls:
        if element['id'] == id:
            element['date_'] = payroll.date_
            element['activity'] = payroll.activity
            element['category'] = payroll.category
            element['responsible'] = payroll.responsible
            element['observation'] = payroll.observation
            return JSONResponse(content={
            "message": "The payroll was updated successfully",
            "data": element
            }, status_code=200)
    return JSONResponse(content={
    "message": "The payroll does not exists",
    "data": None
    }, status_code=404)

@payroll_router.delete('/payrolls/{id}',tags=['payrolls'],response_model=dict,description="Removes specific payroll")
def remove_payroll(id: int = Path(ge=1)) -> dict:
    for element in payrolls:
        if element['id'] == id:
            payrolls.remove(element)
            return JSONResponse(content={
            "message": "The payroll was removed successfully",
            "data": None
            }, status_code=204)
    return JSONResponse(content={
    "message": "The payroll does not exists",
    "data": None
    }, status_code=404)
