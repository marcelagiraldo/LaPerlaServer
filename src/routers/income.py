from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.income import Income

income_router = APIRouter()

incomes = [
    {
        "id": 1,
        "date_": "2024-06-13",
        "category": "Café",
        "price": "500000",
        "description": "Café pergamino seco"
    },
    {
        "id": 2,
        "date_": "2024-06-11",
        "category": "Platano",
        "price": "200000",
        "description": "Platano verde"
    }
]

#-----------------CRUD------------------------
@income_router.get('/incomes',
         tags=['incomes'],
         response_model=List[Income],
         description="Returns all products stored")
def get_all_products() -> List[Income]:
    result = []
    for element in incomes:
        result.append(element)
    return JSONResponse(content=result, status_code=200)

@income_router.get('/incomes/{id}',
         tags=['incomes'],
         response_model=Income,
         description="Returns data of one specific product")
def get_product(id: int = Path(ge=0, le=5000)) -> Income:
    for element in incomes:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content=None, status_code=404)

@income_router.post('/incomes',
          tags=['incomes'],
          response_model=dict,
          description="Creates a new product")
def create_product(income: Income = Body()) -> dict:
    incomes.append(income.model_dump())
    return JSONResponse(content={
        "message": "The product was created successfully",
        "data": income.model_dump()
    }, status_code=201)

@income_router.put('/incomes/{id}',tags=['incomes'],response_model=dict,description="Updates the data of specific income")
def update_income(id: int = Path(ge=1),income: Income = Body()) -> dict:
    for element in incomes:
        if element['id'] == id:
            element['date_'] = income.date_
            element['category'] = income.category
            element['price'] = income.price
            element['description'] = income.description
            element['observation'] = income.observation
            return JSONResponse(content={
            "message": "The income was updated successfully",
            "data": element
            }, status_code=200)
    return JSONResponse(content={
    "message": "The income does not exists",
    "data": None
    }, status_code=404)

@income_router.delete('/incomes/{id}',tags=['incomes'],response_model=dict,description="Removes specific income")
def remove_income(id: int = Path(ge=1)) -> dict:
    for element in incomes:
        if element['id'] == id:
            incomes.remove(element)
            return JSONResponse(content={
            "message": "The product wass removed successfully",
            "data": None
            }, status_code=204)
    return JSONResponse(content={
    "message": "The product does not exists",
    "data": None
    }, status_code=404)
