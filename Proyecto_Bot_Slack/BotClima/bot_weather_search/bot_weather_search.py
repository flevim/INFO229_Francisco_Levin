#!/usr/bin/env python
import pika
import os
import random
import requests
import json
from geopy.geocoders import Nominatim 
import sys 
import time
from datetime import datetime 
import argparse
from tinydb import TinyDB, Query 
import tabulate

time.sleep(30)


########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'ultiminio'
channel.exchange_declare(exchange='ultiminio', exchange_type='topic', durable=True)


#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="weather", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='ultiminio', queue=queue_name, routing_key="weather")

def parse_data_daily(data):
    msg = ""
    dt = datetime.fromtimestamp(int(data['dt'])).strftime('%d-%m-%Y %H:%M:%S')
    temp_min, temp_max = '%s °C' % (data['temp']['min']), '%s °C' % (data['temp']['max'])
    temp_day = '%s °C' % (data['temp']['morn'])
    temp_eve = '%s °C' % (data['temp']['eve']) 
    temp_night = '%s °C' % (data['temp']['night'])
    humidity = '{} %'.format(data['humidity'])
    weather = data['weather'][0]['description']
    pressure = "%s Pa" % (data['pressure'])
    wind_speed = '%s m/s' % (data['wind_speed'])

    headers = ['Item','Valor']
    table = [["Fecha",dt],["Temp mínima",temp_min],["Temp máxima", temp_max], ["Temp mañana", temp_day], 
    ["Temp tarde",temp_eve], ["Temp noche", temp_night], ["Humedad", humidity], ["Descripción", weather], ["Presión", pressure], ["Velocidad viendo", wind_speed]]
    msg = msg + tabulate.tabulate(table, headers, tablefmt="github") + '\n=================================================\n'
    return msg

def get_msg(ciudad):
    print("SE EJECUTÓ GET_MSG")
    geolocator = Nominatim(user_agent="geolocation_places")
    api_key = os.environ['WEATHER_API_KEY']
    parser = argparse.ArgumentParser()

    #Crear tablas de BD
    db = TinyDB('openw_db.json')
    Location = db.table('Location')
    Profile = db.table('Profile')

    # Locación a consultar

    try:
        loc = geolocator.geocode(ciudad)
        lat, long = loc.latitude, loc.longitude
        print("Ciudad: %s ----> Latitude: %s | Longitude: %s" % (ciudad, lat, long))
        
    except AttributeError:
        print("No ha sido posible encontrar este lugar.")
        sys.exit(0)


    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely&units=metric&lang=es&appid=%s" % (lat, long, api_key)

    response = requests.get(url)
    data = json.loads(response.text)

    if 'cod' in data.keys():
        print(data['cod'])
        sys.exit(0)


    lat = data["lat"]
    lon = data["lon"]
    timezone = data["timezone"]
    hourly = data["hourly"]
    daily = data["daily"][0:3]

    msg = "LAT  " + str(lat) + "\n\nLON  " + str(lon) + "\n\nTIMEZONE  " + str(timezone)


    ###############################
    #  PARSEANDO DATA IMPORTANTE  #
    ###############################

    msg = msg + "\n\n-----------------------------------------" + "Pronostico semanal" + "------------------------------------------\n\n"


    for day in daily: 
        msg1 = parse_data_daily(day)
        msg = msg + msg1
    return msg



##########################################################


########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')



def callback(ch, method, properties, body):
    print("hola se ejecutó el CALBACK")
    print(body)
    if str(body).startswith("b'[clima]"):
        print("Esto podría funcionar")
        query = str(body)[9:-1]
        result = get_msg(str(query))
        print(query)
        print(result)

        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        channel.basic_publish(exchange='ultiminio', routing_key="publicar_slack", body=result)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################
