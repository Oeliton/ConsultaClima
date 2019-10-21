# -*- coding: utf-8 -*-

import json
import os
import requests
import historyController
from flask import Flask, jsonify, request

app = Flask(__name__)

#Rota para chamada da API OpenWeather
@app.route("/buscaclimacid", methods=['GET'])
def weather():
    print("teste")
    cityReq = request.args.get('city', None)
    city = cityReq.replace('"','')
    city = cityReq.replace("'","")

    #key OpenWeather (Alterar conforme cadastro)
    myKey = 'b434ece8bfe31d3643e8986e5ff00f46'   
    host = 'http://api.openweathermap.org/data/2.5/forecast'
 
    params={'q': city,'APPID': myKey} 

    r = requests.get(host,params)  
    reqJson = r.json()
    
    if reqJson.get('cod') == '404':
        return jsonify(context=reqJson)

    #Grava dados de hitorico
    #historyController.saveHitory(reqJson)
    
    return jsonify(context=reqJson)

#Rota para busca das gravocoes de historicos de consulta
@app.route("/history", methods=['GET'])
def history():

    cityReq = request.args.get('city', None)
    cityReq = cityReq.replace('"','')
    cityReq = cityReq.replace("'","")    

    #history = historyController.returnHistory(cityReq)
    
    #return jsonify(context=history)
    
if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 6000))
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=port, debug=True)