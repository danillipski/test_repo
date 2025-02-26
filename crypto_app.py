from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class New_Crypto(BaseModel):
    token_id: str
    token_name: str
    token_supply: float 
    #additional_links: dict

@app.get("/")
def home_page():
    return {"Message" : "Hello, World!"} 

@app.get("/user/me")
def my_profile():
    return {"user_name" : "me", "portfolio" : "1,000 USD"}  


@app.get("/user/{userid}")
def user_profile(userid: int):
    return {f"user_name" : {userid}, "portfolio" : "private"}

@app.post("/create/crypto")
async def create_new_crypto(crypto: New_Crypto):
    return {crypto}
