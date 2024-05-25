from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import HTMLResponse, JSONResponse

test_router = APIRouter()

@test_router.get('/')
def greet():
    return "Hello World"

@test_router.get('/hello',tags=["web"],description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World TEST</h1>")
