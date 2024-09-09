from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.routers as routers

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:80",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://localhost:80",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def read_root():
    return {"status": "success"}


app.include_router(routers.block_router, prefix="/blocks")
