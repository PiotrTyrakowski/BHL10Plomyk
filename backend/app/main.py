from fastapi import FastAPI
from .routers import users, certificates, missions, recommendations, statistics, auth
from .database.database import Base, engine
from .middleware.logging import LoggingMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(certificates.router)
app.include_router(missions.router)
app.include_router(recommendations.router)
app.include_router(statistics.router)
