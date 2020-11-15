#-*- coding: utf-8 -*-

#import psutil
import time
import signal
import sys
import requests
import urllib.parse
import json

import Adafruit_BMP.BMP085 as BMP085

#variable1 = 0
variable2 = 0

sensor = BMP085.BMP085()


def cpu_ram(variable1,cont):
    while True:
        
        #Obtener datos del sensor
        temp = sensor.read_temperature()
        pressure = sensor.read_pressure()
        altitude = sensor.read_altitude()
        sealevelpres = sensor.read_sealevel_pressure()
        cont = cont + 1
        #Mostrar datos btenidos en pantalla
        print(str(cont) + "\tTemperatura: " + str(temp) + " C\tPresion: " + str(pressure) + " Pa\tAltitud: " + str(altitude) + " m\tPresion Nivel Del Mar: " + str(sealevelpres) + ' Pa')

        metodo = 'POST'     #Añadir datos al canal
        uri = "https://api.thingspeak.com/update.json"
        cabeceras = {'Host': 'api.thingspeak.com',
                     'Content-Type': 'application/x-www-form-urlencoded'}
        contenido = {'api_key': variable1,
                     'field1': temp,
                     'field2': pressure,
                     'field3': altitude,
                     'field4':sealevelpres}
        contenido_encoded = urllib.parse.urlencode(contenido)
        cabeceras['Content-Length'] = str(len(contenido_encoded))
        respuesta = requests.request(metodo, uri, data=contenido_encoded,
                                     headers=cabeceras, allow_redirects=False)
        codigo = respuesta.status_code
        descripcion = respuesta.reason
        #print(str(codigo) + " " + descripcion)
        contenido = respuesta.content
        #print(contenido)

        time.sleep(15)

def handler(sig_num, frame):    #El evento es para parar el proceso
    # Gestión del evento
    print('\nSignal handler called with signal ' + str(sig_num))
    print('Check signal number on ' 'https://en.wikipedia.org/wiki/Signal_%28IPC%29#Default_action')

    var_str=str(variable2)    #Borrar datos del canal
    metodo = 'DELETE'
    uri = "https://api.thingspeak.com/channels/"+var_str+"/feeds.json"
    cabeceras = {'Host': 'api.thingspeak.com',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    contenido = {'api_key': 'LFG2I039JEF48ZBH'
                 }
    contenido_encoded = urllib.parse.urlencode(contenido)
    cabeceras['Content-Length'] = str(len(contenido_encoded))
    respuesta = requests.request(metodo, uri, data=contenido_encoded,
                                 headers=cabeceras, allow_redirects=False)
    codigo = respuesta.status_code
    descripcion = respuesta.reason
    print(str(codigo) + " " + descripcion)
    contenido = respuesta.content
    #print(contenido)

    print('\nExiting gracefully')
    sys.exit(0)


if __name__ == "__main__":

    metodo = 'POST'   #Crear canal
    uri = "https://api.thingspeak.com/channels.json"
    cabeceras = {'Host': 'api.thingspeak.com',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    contenido = {'api_key': 'LFG2I039JEF48ZBH',
                 'name': 'Estacion Barometrica',
                 'field1': "Temperatura (ºC)",
                 'field2': "Presion (Pa)",
                 'field3': "Altitud (m)",
                 'field4': "Presion Nivel Del Mar (Pa)"}
    contenido_encoded = urllib.parse.urlencode(contenido)
    cabeceras['Content-Length'] = str(len(contenido_encoded))
    respuesta = requests.request(metodo, uri, data=contenido_encoded,
                                 headers=cabeceras, allow_redirects=False)
    codigo = respuesta.status_code
    descripcion = respuesta.reason
    print(str(codigo) + " " + descripcion)
    contenido = respuesta.content
    #print(contenido)

    y = json.loads(contenido)
    variable1 = y['api_keys'][0]['api_key']
    variable2 = y['id']
    print(variable1)
    print(variable2)

    signal.signal(signal.SIGINT, handler)
    print('Running. Press CTRL-C to exit.')
    cont = 0
    cpu_ram(variable1,cont)
    while True:
        pass # No hacer nada
