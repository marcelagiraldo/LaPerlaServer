from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.category import Category
category_router = APIRouter()


categories = [
    {
        "id": 1,
        "name": "Café"
    },
    {
        "id": 2,
        "name": "Platano"
    }
]

#-----------------CRUD------------------------
@category_router.get('/categories',
tags=['categories'],
response_model=List[Category],
description="Returns all categories stored")
def get_all_categories() -> List[Category]:
    result = []
    for element in categories:
        result.append(element)
    return JSONResponse(content=result, status_code=200)

@category_router.get('/categories/{id}',tags=['categories'],response_model=Category,
description="Returns data of one specific expense")
def get_category(id: int = Path(ge=1, le=5000)) -> Category:
    for element in categories:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content=None, status_code=404)

@category_router.post('/categories',
          tags=['categories'],
          response_model=dict,
          description="Creates a new product")
def create_product(category: Category = Body()) -> dict:
    categories.append(category.model_dump())
    return JSONResponse(content={
        "message": "The product was created successfully",
        "data": category.model_dump()
    }, status_code=201)

@category_router.put('/categories/{id}',tags=['categories'],response_model=dict,description="Updates the data of specific expense")
def update_category(id: int = Path(ge=1),category: Category = Body()) -> dict:
    for element in categories:
        if element['id'] == id:
            element['name'] = category.name
            return JSONResponse(content={
            "message": "The expense was updated successfully",
            "data": element
            }, status_code=200)
    return JSONResponse(content={
    "message": "The expense does not exists",
    "data": None
    }, status_code=404)

@category_router.delete('/categories/{id}',tags=['categories'],response_model=dict,description="Removes specific expense")
def remove_category(id: int = Path(ge=1)) -> dict:
    for element in categories:
        if element['id'] == id:
            categories.remove(element)
            return JSONResponse(content={
            "message": "The expense was removed successfully",
            "data": None
            }, status_code=204)
    return JSONResponse(content={
    "message": "The expense does not exists",
    "data": None
    }, status_code=404)
