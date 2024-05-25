from fastapi import FastAPI

from src.middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware
from src.routers.user import user_router
from src.routers.test import test_router

#########################################################
app = FastAPI()

app.title = "User API"
app.summary = "User REST API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.1"
app.contact = {
    "name": "Marcela Alzate",
    "url": "",
    "email": "lmarceag@gmail.com",
}
# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],)
#########################################################
app.openapi_tags = [
    {
        "name": "web",
        "description": "Endpoints of example",
    },
    {
        "name": "users",
        "description": "user handling endpoints",
    },
]

########################################################
#Midelware
app.add_middleware(ErrorHandler)

########################################################
## Router's definition (endpoints sets)
app.include_router(prefix="/user", router=user_router)
app.include_router(prefix="/test", router=test_router)





