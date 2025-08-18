from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome mate!"}

@app.get("/posts")
def get_posts():
    return {"data": "get_posts data"}

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/create_posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())