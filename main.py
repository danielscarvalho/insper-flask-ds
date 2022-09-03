import os
from flask import Flask
from flask import request
from datetime import datetime
import insperds
import math

app = Flask(__name__)

@app.route('/')
def web_root():
    now = datetime.now()
    return 'Hey, we have Flask in a Docker container by Insper DS! - ' + str(now) 

@app.route('/core')
def core():
    now = datetime.now()
    return 'Vai Corinthians!! - ' + str(now) 

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(float(a) + float(b))

@app.route('/area')
def myarea():
  altura = request.args.get('altura', default = 0, type = float)
  largura = request.args.get('largura', default = 0, type = float)
  comprimento = request.args.get('comprimento', default = -1, type = float)
  
  if (comprimento < 0):
        return str(altura*largura)
  else:
        return str(altura*largura*comprimento)

@app.route('/query/<text>')
def query(text):
    return insperds.ddgquery(text)
    
@app.route('/bitcoins')
def btc():
    return insperds.bitcoins()
    
@app.route('/ethereum')
def ether():
    return insperds.ethereum()
    
@app.route('/weather/<lat>/<lon>')
def weather(lat, lon):
    return insperds.weather(lat, lon)

@app.route('/safepassword', defaults={'size': ""})
@app.route('/safepassword/<size>')
def pwd(size):
    if (len(size)>0):
        return insperds.newpassword(int(size))
    else: 
        return insperds.newpassword()

@app.route('/sub/<a>/<b>')
def sub(a, b):
    return str(float(a) - float(b))

@app.route('/power/<a>/<b>')
def ipower(a, b):
    a_float = float(a)
    
    try:
        b_float = float(b)
    except:
        return str(a_float * a_float)
    
    return str(math.pow(a_float, b_float))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
