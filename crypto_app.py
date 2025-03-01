from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

def add_id(database, dict_token):
    previous_id = len(database)
    id = previous_id + 1
    dict_token.update({"id": id})
    print(id)
    return id

def update_id(id, database, dict_token):
    for x in database:
        if x["id"] == id:
            x.update(dict_token)  
            print(x)
            break
            return x


class Token(BaseModel):
    token_id: str
    token_name: str
    token_supply: int 
    #additional_links: dict

database = [{"token_id": "row", "token_name": "rowbow", "token_supply": 100, "id": 1}, {"token_id": "rai", "token_name": "rain", "token_supply": 10000, "id": 2}]

@app.get("/")
def home_page():
    return {"Message" : "Hello, World!"} 

@app.get("/user/me")
def my_profile():
    return {"user_name" : "me", "portfolio" : "1,000 USD"}  


@app.get("/user/{userid}")
def user_profile(userid: int):
    return {"user_name" :userid, "portfolio" : "private"}

# Here is how to extract the data from the Body # Body is a property???
@app.post("/crypto/create/", status_code=201)
def create_new_crypto(token: Token):
    dict_token = dict(token)
    database.append(dict_token)
    add_id(database, dict_token)
    print(database[-1])

    return {"data": dict_token}


@app.put("/crypto/create/{id}", status_code=201)
def update_crypto(id: int, token: Token):
    dict_token = dict(token)
    update_id(id, database, dict_token)
    return {"new data": dict_token}