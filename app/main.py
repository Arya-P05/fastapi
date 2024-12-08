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
    for idx, post in enumerate(my_posts):
        if post["id"] == id:
            return idx
    
    return "not found"

def delete_post_from_id(id):
    for idx in range(len(my_posts)):
        if my_posts[idx]["id"] == id:
            my_posts.pop(idx)

# Known as a path operation or route:
@app.get("/") # decorator (@), fastapi instance (app), hppt method (.get), route path ("/")
def root():
    return {"message": "hi chakliii"}

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
    post = my_posts[get_post_from_id(id)]

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found!")
    else:
        return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    if get_post_from_id(id) == "not found":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found.")
    delete_post_from_id(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    post_idx = get_post_from_id(id)
    
    if post_idx == "not found":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found.")
    
    new_updated_post = post.model_dump()
    new_updated_post["id"] = id

    my_posts[post_idx] = new_updated_post
    return {"data": new_updated_post}
