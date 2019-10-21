#Classe dos historicos de consulta da API
class History(object):
    
    def __init__(self, temp_max,temp_min,date_forecast,date_query,weather,id_city):
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.date_forecast = date_forecast
        self.date_query = date_query
        self.weather = weather
        self.id_city = id_city

    def getTemp_max(self):
        return self.temp_max

    def getTemp_min(self):
        return self.temp_min

    def getDate_forecast(self):
        return self.date_forecast        

    def getDate_query(self):
        return self.date_query

    def getWeather(self):
        return self.weather

    def getId_city(self):
        return self.id_city                        

    def setTemp_max(self, temp_max):
        self.temp_max = temp_max

    def setTemp_min(self, temp_min):
        self.temp_min = temp_min        

    def setDate_forecast(self, date_forecast):
        self.date_forecast = date_forecast

    def setDate_query(self, date_query):
        self.date_query = date_query

    def setWeather(self, weather):
        self.weather = weather

    def setId_city(self, id_city):
        self.id_city = id_city     