# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:06:49 2019

@author: oeliton.cappelletto
"""

from Data import connectdb
from Model import history

cur = connectdb.getCursor()
con = connectdb.getConnection()

def save(temp_max,temp_min,date_forecast,date_query,weather,id_city):
    sql = str("insert into history_weather (temp_max,temp_min,date_forecast,date_query,weather,id_city) " +
              " values (%s,%s,%s,%s,%s,%s)")
    cur.execute(sql, [temp_max,
                      temp_min,
                      date_forecast,
                      date_query,
                      weather,
                      id_city])
    con.commit()

def select(name):

    sql = str(  'SELECT                                   '+
                '    temp_max,                            '+
                '    temp_min,                            '+
                '    date_forecast,                       '+
                '    date_query,                          '+
                '    weather,                             '+
                '    id_city                              '+
                'FROM                                     '+
                '    history_weather                      '+
                'JOIN city ON                             '+
                '    city.id = history_weather.id_city    '+
                'WHERE                                    '+
                '    city.name = %s                       ')

    cur.execute(sql, [name])
    
    recset = cur.fetchall()

    weatherList = []
    for rec in recset:
        
        hist = history.History(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5])
       
        weather = dict(temp_max = hist.getTemp_max(),temp_min = hist.getTemp_min(),date_forecast = hist.getDate_forecast(),date_query = hist.getDate_query(),weather = hist.getWeather(),id_city = hist.getId_city())
        weatherList.append(weather)
        
    return weatherList