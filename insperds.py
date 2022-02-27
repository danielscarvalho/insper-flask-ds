import requests

def ddgquery(query):
    URL = "https://api.duckduckgo.com/?format=json&pretty=0&q=" + query
    response = requests.get(URL)
    ddg = response.json()
    info = ddg["Abstract"]
    if len(info) > 1:
        return info
    else:
    	return "Ops! No data found!" 

def bitcoins():
    URL="https://www.mercadobitcoin.net/api/BTC/trades/"
    response = requests.get(URL)
    return {"btc":response.json()}

def ethereum():
    URL="https://www.mercadobitcoin.net/api/ETH/trades/"
    response = requests.get(URL)
    return {"eth":response.json()}

def weather(latitude, longitude):
    KEY = "ed38d2abac6e6aded3cf1ed68fddb3c6"
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat=' + str(latitude) + '&lon=' + str(longitude) + '&appid='+ KEY
    return requests.get(URL).json()

# Teste	
# print(ddgquery("Madonna"))
# print(ddgquery("Duckduckgo"))
# print(ethereum())
# print(weather(-23.5984834927,-46.6766234833))
