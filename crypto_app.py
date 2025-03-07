from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Crypto(BaseModel):
    CA: str


def create_pair_to_database():
    pass


while True: 
    try: 
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="*******", port=5432, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print("Database connection was succesfull!")
        break
        
    except Exception as error:
        print("Database connection has failed")
        print(f"The error was: {error}")
        time.sleep(3)


@app.get("/")
def home_page():
    return {"message": "Welcome to Token Trade!"}


@app.post("/crypto/{CA}")
def create_pair(CA: int):
    curr.execute()