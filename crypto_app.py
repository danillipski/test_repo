from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()
while True: 
    try: 
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="**************", port=5432, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print("Database connection was succesfull!")
        break
        
    except Exception as error:
        print("Database connection has failed")
        print(f"The error was: {error}")
        time.sleep(3)


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
            return x
            

def find_id(id, database):
    for x in database:
        if x["id"] == id:
            return x

def delete_id(id, database):
    for x in database:
        if x["id"] == id:
            database.pop()




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


#@app.get("/crypto/{id}")
#def crypto_id(id: int):
#    token_id = find_id(id, database)
#    return {"pair id" : id, "data" : token_id}

@app.get("/crypto/{CA}")
def crypto_id(CA: str):
    CA_corrected = ("'"+ CA +"'")  
    cur.execute(f'SELECT * FROM crypto_pairs WHERE "CA" = {CA_corrected}')
    crypto_pair = cur.fetchall()
    print(crypto_pair)
    return {"crypto_pair" : crypto_pair}

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
    update_token = update_id(id, database, dict_token)
    return {"new data": update_token} 


@app.delete("/crypto/{id}")
def delete_crypto(id: int):
    delete_id(id, database)
    print(database, end=" ")
    return {"id": id, "message" : "was succesfully deleted"}