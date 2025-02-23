### This is an API Page ###

#import requests

#Token_adress = input("Token_adress? :")
#response = requests.get(url=f"https://api.dexscreener.com/latest/dex/pairs/solana/{Token_adress}")

#data = response.json()

#====================================================================================================#

# Discord Bot dev tasks #
# 
# 1) Send CA , price
# 2) link to descreen
# 3) additional info
# It has to be formated in kinda tab like RICK BOT


# Crypto Arbitrage Bot  dev tasks #
#
# 1) scan every single pair (at the start can start with limited num of pairs) from a few different excnahges
# 2) while scanning it should search fro the price
# 3) then it should calculate on itself the difference  
# 4) If difference is big enough including fees for sending = print this pairs and excnahges out
import python_proficiency

west_road1 = West_Road(100)
print(west_road1)

# Test syncronous / asynchronous
import asyncio
import time
#Bitcoin == 60.000
#class Bitcoin():

 #   def __init__(self):
  #      pass

   # for second in time.sleep(100000000000000000):

    #    print(second)

    
#class Binance(Bitcoin)
        

#bitcoin1 = Bitcoin



async def fetch_data(time_sleep, id, data):
    print(f"Starting the process...")
    await asyncio.sleep(time_sleep)
    print(f"id: {id}, awited time: {time_sleep}, data: {data}")


async def  main():
    print(f"Ready to process data...")
    data1 = asyncio.create_task(fetch_data(3, 1, {"name" : "Alex"}))
    data2 = asyncio.create_task(fetch_data(2, 2, {"name" : "Roma"}))
    data3 = asyncio.create_task(fetch_data(1, 3, {"name" : "Danil"}))
    print(f"All done!")
    result1 = await data1
    result2 = await data2
    result3 = await data3
    return {result1, result2, result3}


#async with asyncio.TaskGroup() as gt:


asyncio.run(main())
