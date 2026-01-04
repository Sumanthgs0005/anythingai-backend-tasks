from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import auth_routes, task_routes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AnythingAI Tasks API",
    version="1.0.0",
    description="Scalable REST API with authentication & role-based access for tasks.",
)

# CORS (allow frontend on same machine)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",  # e.g., Live Server or simple static host
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for assignment you can keep it open
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
