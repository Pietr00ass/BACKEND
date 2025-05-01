from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .dependencies import engine
from .models import Base
from .routers import auth, crypto, ocr

app = FastAPI(title="Cryptonet API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    # create tables
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(crypto.router, prefix="/crypto", tags=["crypto"])
app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])

@app.get("/")
def root():
    return {"message": "Cryptonet API is running"}
