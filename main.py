### Discord bot is here


import discord
import aiohttp
import requests

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged on as a {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("hello"):
        await message.channel.send("Hello!")
        print(message.content)
        

    if message.content == "6kchu2zebjgv27sevdquvcsgfrnx6xgcgyhqalqneyy9":
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url="https://api.dexscreener.com/latest/dex/pairs/solana/6kchu2zebjgv27sevdquvcsgfrnx6xgcgyhqalqneyy9", headers={}) as response:
        #response = requests.get(url="https://api.dexscreener.com/latest/dex/pairs/solana/6kchu2zebjgv27sevdquvcsgfrnx6xgcgyhqalqneyy9", headers={})
                data = await response.json()
                mcap = data["pair"]["marketCap"]
                price = data["pair"]["priceUsd"]
                await message.channel.send(f"The mcap is {mcap}, and the price is {price}")



client.run('""""**********""""')