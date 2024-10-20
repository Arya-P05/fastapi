from fastapi import FastAPI, Response, status
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

def get_post_from_id(id) :
    for post in my_posts:
        if post["id"] == id:
            return post

# Known as a path operation or route:
@app.get("/") # decorator (@), fastapi instance (app), hppt method (.get), route path ("/")
def root():
    return {"message": "hi chakli"}

@app.get("/posts/")
def get_posts():
    return {"data": my_posts}

@app.post("/posts/")
def create_posts(payload: Post):
    # return {"title": f"{payload.title}", "content": f"{payload.content}", "is_post_public": payload.public, "rating": payload.rating}
    post_dict = payload.model_dump()
    post_dict["id"] = randint(0, 1000000)
    my_posts.append(post_dict)
    return post_dict

@app.get("/posts/{id}") # this id field is known as a path parameter
def get_one_post(id: int, response: Response):
    post = get_post_from_id(id)

    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Message": f"Post with id: {id} was not found!"}
    return post
