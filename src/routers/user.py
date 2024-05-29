from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.user import User

user_router = APIRouter()


users = [
    {
        "id": 1,
        "user": "oscar",
        "password": "hola123",
        "name": "Oscar Alzate",
        "email": "none",
        "rol":"user"
    }
]

#-----------------CRUD------------------------
@user_router.get('/users',
tags=['users'],
response_model=List[User],
description="Returns all users stored")
def get_all_users(min_price: float = Query(default=None, min=10, max=5000000),
                    max_price: float = Query(default=None, min=10, max=5000000)) -> List[User]:
    result = []
    for element in users:
        result.append(element)
    return JSONResponse(content=result, status_code=200)

@user_router.get('/users/{id}',tags=['users'],response_model=User,
description="Returns data of one specific user")
def get_user(id: int = Path(ge=1, le=5000)) -> User:
    for element in users:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content=None, status_code=404)

@user_router.post('/users',tags=['users'],response_model=dict,description="Creates a new user")
def create_user(user: User = Body()) -> dict:
    users.append(user.model_dump())
    return JSONResponse(content={"message": "The user was created successfully",
        "data": user.model_dump()
    }, status_code=201)

@user_router.put('/users/{id}',tags=['users'],response_model=dict,description="Updates the data of specific user")
def update_user(id: int = Path(ge=1),user: User = Body()) -> dict:
    for element in users:
        if element['id'] == id:
            element['user'] = user.user
            element['password'] = user.password
            element['name'] = user.name
            element['email'] = user.email
            element['rol'] = user.rol
            return JSONResponse(content={
            "message": "The user was updated successfully",
            "data": element
            }, status_code=200)
    return JSONResponse(content={
    "message": "The user does not exists",
    "data": None
    }, status_code=404)

@user_router.delete('/users/{id}',tags=['users'],response_model=dict,description="Removes specific user")
def remove_user(id: int = Path(ge=1)) -> dict:
    for element in users:
        if element['id'] == id:
            users.remove(element)
            return JSONResponse(content={
            "message": "The product wass removed successfully",
            "data": None
            }, status_code=204)
    return JSONResponse(content={
    "message": "The product does not exists",
    "data": None
    }, status_code=404)
