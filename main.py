import os
from flask import Flask
from flask import request
from datetime import datetime
import platform
import insperds
import math

app = Flask(__name__)

@app.route('/')
def web_root():
    now = str(datetime.now())
    return 'Hey, we have Flask in a Docker container by Insper DS! - ' + now + ' - ' + str(platform.version) 

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

@app.route('/num/<a>/<b>')
def num(a, b):
    a_f = float(a)
    b_f = float(b)
    if a_f % 2 == 0:
        return str(a_f**b_f)
    else:
        return str(a_f - b_f)

@app.route('/power/<a>')
def power1(a):
    a_float = float(a)
    
    return str(a_float * a_float)
        
@app.route('/power/<a>/<b>')
def power2(a, b):
    a_float = float(a)
    b_float = float(b)
    
    return str(math.pow(a_float, b_float))

@app.route('/calc/<a>/<b>')
def calc(a, b):
    a_float = float(a)
    b_float = float(b)
    
    return str((1-math.pow(a_float, b_float))*math.sqrt(a_float))

@app.route('/icalc/<x>')
def icalcweb(x):
    return str(insperds.icalc(float(x)))

@app.route('/catfact')
def icatfact():
    return insperds.catfact()
    
@app.route('/media/<m>/<n>')
def media(m, n):
    return str((float(m)+float(n))/2)    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
