from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import routers

app = FastAPI(
    title="FindMyJob - API",
    description="FastAPI project",
    version="0.1.0",
    contact={
        "name": "Daniil Kozhushko",
        "url": "https://daniilkozhushko.com"
    }
)

# подключение всех найденных роутеров
for r in routers:
    app.include_router(r)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the FindMyJob API 🚀",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )