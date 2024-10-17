from fastapi import FastAPI

app = FastAPI()

# Known as a path operation or route:
@app.get("/") # decorator (@), fastapi instance (app), hppt method (.get), route path ("/")
def root():
    return {"message": "hi chakli"}

@app.get("/get_posts/")
def get_posts():
    return {"data": "post details"}