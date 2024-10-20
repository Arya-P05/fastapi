from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randint

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    public: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "i like pizza", "id": 2}]

def get_post_from_id(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def delete_post_from_id(id):
    for idx in range(len(my_posts)):
        if my_posts[idx]["id"] == id:
            my_posts.pop(idx)

# Known as a path operation or route:
@app.get("/") # decorator (@), fastapi instance (app), hppt method (.get), route path ("/")
def root():
    return {"message": "hi chakli"}

@app.get("/posts/")
def get_posts():
    return {"data": my_posts}

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_posts(payload: Post):
    # return {"title": f"{payload.title}", "content": f"{payload.content}", "is_post_public": payload.public, "rating": payload.rating}
    post_dict = payload.model_dump()
    post_dict["id"] = randint(0, 1000000)
    my_posts.append(post_dict)
    return post_dict

@app.get("/posts/{id}") # this id field is known as a path parameter
def get_one_post(id: int):
    post = get_post_from_id(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found!")
    else:
        return post

@app.delete("/posts/{id}")
def delete_post(id: int):
    delete_post_from_id(id)
    return {"Message": "Post deleted!"}