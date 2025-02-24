from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#class Model(BaseModel):
    #pass

@app.get("/")
def home_page():
    return {"Message" : "Hello, World!"} 

@app.get("/user/me")
def my_profile():
    return {"user_name" : "me", "portfolio" : "1,000 USD"}  


@app.get("/user/{userid}")
def user_profile(userid: int):
    return {f"user_name" : {userid}, "portfolio" : "private"}
