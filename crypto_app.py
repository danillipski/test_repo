import requests

Token_adress = input("Token_adress? :")
response = requests.get(url=f"https://api.dexscreener.com/latest/dex/pairs/solana/{Token_adress}")

data = response.json()

print(data)