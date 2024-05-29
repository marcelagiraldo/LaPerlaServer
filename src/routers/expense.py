from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.expense import Expense
expense_router = APIRouter()


expenses = [
    {
        "id": 1,
        "date_": "2024-06-13",
        "category": "Café",
        "price": "30000",
        "desciption": "Compra de abono",
        "observation":""
    },
    {
        "id": 2,
        "date_": "2024-06-11",
        "category": "Platano",
        "price": "50000",
        "desciption": "Compra de veneno",
        "observation":"Veneno para el picudo"
    }
]

#-----------------CRUD------------------------
@expense_router.get('/expenses',
tags=['expenses'],
response_model=List[Expense],
description="Returns all expenses stored")
def get_all_expenses(min_price: float = Query(default=None, min=10, max=5000000),
                    max_price: float = Query(default=None, min=10, max=5000000)) -> List[Expense]:
    result = []
    for element in expenses:
        result.append(element)
    return JSONResponse(content=result, status_code=200)

@expense_router.get('/expenses/{id}',tags=['expenses'],response_model=Expense,
description="Returns data of one specific expense")
def get_expense(id: int = Path(ge=1, le=5000)) -> Expense:
    for element in expenses:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content=None, status_code=404)

@expense_router.post('/expenses',
          tags=['expenses'],
          response_model=dict,
          description="Creates a new product")
def create_product(expense: Expense = Body()) -> dict:
    expenses.append(expense.model_dump())
    return JSONResponse(content={
        "message": "The product was created successfully",
        "data": expense.model_dump()
    }, status_code=201)

@expense_router.put('/expenses/{id}',tags=['expenses'],response_model=dict,description="Updates the data of specific expense")
def update_expense(id: int = Path(ge=1),expense: Expense = Body()) -> dict:
    for element in expenses:
        if element['id'] == id:
            element['date_'] = expense.date_
            element['category'] = expense.category
            element['price'] = expense.price
            element['desciption'] = expense.desciption
            element['observation'] = expense.observation
            return JSONResponse(content={
            "message": "The expense was updated successfully",
            "data": element
            }, status_code=200)
    return JSONResponse(content={
    "message": "The expense does not exists",
    "data": None
    }, status_code=404)

@expense_router.delete('/expenses/{id}',tags=['expenses'],response_model=dict,description="Removes specific expense")
def remove_expense(id: int = Path(ge=1)) -> dict:
    for element in expenses:
        if element['id'] == id:
            expenses.remove(element)
            return JSONResponse(content={
            "message": "The expense was removed successfully",
            "data": None
            }, status_code=204)
    return JSONResponse(content={
    "message": "The expense does not exists",
    "data": None
    }, status_code=404)
