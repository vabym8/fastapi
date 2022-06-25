from fastapi import FastAPI
# from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_password)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
 
@app.get("/")
def root():
    return {"message": "Hello World!!!!"}     

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


