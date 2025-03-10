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
        # Connect to an existing database 
        conn = psycopg2.connect(
            host="localhost", 
            database="fastapi", 
            user="postgres", 
            password="******", 
            port=5432, 
            cursor_factory=RealDictCursor)

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
    Description: Optional[str] = None
    Supply: Optional[int] = None 

class Update_Crypto(BaseModel):
    Description: Optional[str] = None

# Create a function that that creates a new pair in database
def create_pair_to_database(crypto):

    # Convert to a dictionary the schema
    dict_Crypto = crypto.dict()
    
    
    # Cursor database INSERT INTO opperation (INSERT INTO crypto_pairs () VALUES (%s, %s) RETURNING *, ())
    curr.execute(
        """INSERT INTO crypto_pairs ("CA","Token_name", "Token_ID", "Description", "Supply") VALUES (%s, %s, %s, %s, %s) RETURNING *""",

        (

            dict_Crypto['CA'], 
            dict_Crypto['Token_name'], 
            dict_Crypto['Token_ID'], 
            dict_Crypto['Description'], 
            dict_Crypto['Supply']

        ))   

    # Fetch one row and store it in a variable 
    new_pair = curr.fetchone()
    # Commit changes into a database
    conn.commit() 
    # Returning a pair stored in a variable
    return new_pair


def update_pair_in_database(crypto, CA):

    crypto_Dict = crypto.dict()


    curr.execute("""UPDATE crypto_pairs SET "Description" = %s WHERE "CA" = %s RETURNING *""", 
    
    (

        crypto_Dict['Description'],
        CA

    ))

    update_pair = curr.fetchone()
    conn.commit()
    return update_pair
    

def delete_crypto_pair_from_database(CA):
    curr.execute("""DELETE FROM crypto_pairs WHERE "CA" = %s RETURNING *""",

    ( 

        CA,

    ))

    deleted_pair = curr.fetchone()
    conn.commit()
    return deleted_pair


def get_list_of_all_crypto_pairs():
        curr.execute("SELECT * FROM crypto_pairs")
        list_of_pairs = curr.fetchall()
        return list_of_pairs


@app.get("/")
def home_page():
    print("Hello!")
    return {"message": "Welcome to Token Trade!"}


# Path and POST operation 
@app.post("/crypto/new")
# pass a Schema and store in a variable -> crypto
def create_pair(crypto: Crypto):
    # execute a function and store it in a variable
    try:
        new_pair = create_pair_to_database(crypto)
        return {"CA": new_pair['CA'], "data": new_pair}
    except Exception as error:
        print(error)
        return {"404": "Page is not found"}



@app.get("/crypto/pairs")
def get_all_crypto():
    try:
        list_of_pairs = get_list_of_all_crypto_pairs()
        return {"crypto_pairs": list_of_pairs}
    except Exception as error:
        print(error)
        return {"404": "It is not what you looking for"}


@app.put("/crypto/pairs/{CA}")
def update_crypto_pair(CA: str, crypto: Update_Crypto):
    try: 
        update_pair = update_pair_in_database(crypto, CA)
        return {"Update": "Succesfull", "CA": update_pair["CA"], "data": update_pair}
    except Exception as error:
        print(error)
        return {"404": "Page wasnt found!"}


@app.delete("/crypto/pairs/{CA}")
def delete_crypto_pair(CA: str):
    try:
        delete_pair = delete_crypto_pair_from_database(CA)
        deleted_ca = delete_pair["CA"]
        return {f"Pair with CA {deleted_ca}": "Was Succesfully deleted",
        "data:": delete_pair}
    except Exception as error:
        print(error)
        return {"404": "page was not found"}
