from fastapi import FastAPI

from api.routers import solve_result

app = FastAPI()

app.include_router(solve_result.router)
