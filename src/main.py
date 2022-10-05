from fastapi import FastAPI
from .routes.Routes import routes

app = FastAPI()

for route in routes:
    app.include_router(route.router)