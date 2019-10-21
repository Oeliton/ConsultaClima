from datetime import date
from Data import citydb, historydb
from Model import history

def saveHitory(reqJson):
    city = reqJson.get('city')
    nameCity = city.get('name')
    
    #grava cidade
    idCity = citydb.save(nameCity)

    historyList = reqJson.get('list')
    
    date_query = date.today()
    id_city = idCity
    for history in historyList:
        date_forecast = history.get('dt_txt')
        main = history.get('main')
        temp_max = main.get('temp_max')
        temp_min = main.get('temp_min')
        weather = history.get('weather')
        for item in weather:
            weather = item.get('description')
        
        #gravar historico
        historydb.save(temp_max,temp_min,date_forecast,date_query,weather,id_city)
        
def returnHistory(nameCity):
    return historydb.select(nameCity)