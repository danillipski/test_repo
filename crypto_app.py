from typing import Union
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()
while True:
    try: 
        # Connect to an existing database 
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="*********", port=5432, cursor_factory=RealDictCursor)
        # Connect Cursor to perform database operation
        curr = conn.cursor()
        print("Connection to databse was succesfull!")
        break

    except Exception as error: 
        print("Connection to database has failed!")
        print(f"The error was: {error}")
        time.sleep(3)

# Create a Schema
class Crypto(BaseModel):
    CA: str
    Token_name: str
    Token_ID: str
    Description: Union[str, None] = None
    Supply: Union[int, None] = None 

# Create a function that that creates a new pair in database
def create_pair_to_database(crypto):
    # Convert to a dictionary the schema
    dict_Crypto = dict(crypto)
    # Cursor database INSERT INTO opperation (INSERT INTO crypto_pairs () VALUES (%s, %s) RETURNING *, ())
    curr.execute(
        """INSERT INTO crypto_pairs ("CA","Token_name", "Token_ID", "Description", "Supply") VALUES ('%s', '%s', '%s', '%s', '%s') RETURNING *""",
        (dict_Crypto["CA"], dict_Crypto["Token_name"], dict_Crypto["Token_ID"], dict_Crypto["Description"], dict_Crypto["Supply"]))
    # Fetch one row and store it in a variable 
    new_pair_fetch = curr.fetcone()
    # Commit changes into a database
    conn.commit()




@app.get("/")
def home_page():
    print("Hello!")
    return {"message": "Welcome to Token Trade!"}

# Path and POST operation 
@app.post("/crypto/new")
# pass a Schema and store in a variable -> crypto
def create_pair(crypto: Crypto):
    # execute a function and store it in a variable
    new_pair = create_pair_to_database(crypto, dict_Crypto)
    return {"CA":new_pair["CA"], "data": new_pair}