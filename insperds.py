import requests
import random
import string
import statistics

def ddgquery(query):
    URL = "https://api.duckduckgo.com/?format=json&pretty=0&q=" + query
    response = requests.get(URL)
    ddg = response.json()
    info = ddg["Abstract"]
    if len(info) > 1:
        return info
    else:
        res=""

        for topic in ddg['RelatedTopics']:
            try: 
                res += ("- " + topic['Text'] + "\n")
            except:
                # refactor!!!
                pass
        
        if len(res) > 0:
            return res 
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

def newpassword(size=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = characters.replace("'","").replace('"',"").replace("\\","")

    return ''.join(random.choice(characters) for i in range(size))

def icalc(x):
    if x < 0:
        return 0
    else:
        if x % 2 == 0:
            return x**x
        else:
            return x**2
    
def catfact():
    URL="https://catfact.ninja/fact"
    fc_dic = requests.get(URL).json()
    return fc_dic["fact"]


def describer(list):
    data = [float(v) for v in list.split(",")]
    stats = {"mean":statistics.mean(data),
             "mode":statistics.mode(data),
             "stdev":statistics.stdev(data),
             "size":len(data),
             "max":max(data),
             "min":min(data)}

    return str(stats)
 


# Teste	
# print(ddgquery("Madonna"))
# print(ddgquery("Duckduckgo"))
# print(ethereum())
# print(weather(-23.5984834927,-46.6766234833))
# print(newpassword())
# print(newpassword(16))
