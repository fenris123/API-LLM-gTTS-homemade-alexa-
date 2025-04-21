# -*- coding: utf-8 -*-

"""
Created on Wed Mar 12 12:21:08 2025

@author: fenris123
"""



import json
import os
import requests
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta
from time import sleep
from gpt4all import GPT4All
from gtts import gTTS





# PASO 1: CARGA DE TOKEN
load_dotenv("C:/espaciopython/enviroments/tokens.env")
Token_aemet = os.getenv("TOKEN_AEMET")

headers = {
    "accept": "application/json",
    "api_key": Token_aemet
}





# PASO 2: Establecer rango de fechas de la última semana# Obtener la fecha y hora actuales
hoy = datetime.utcnow()


una_semana_atras = hoy - timedelta(days=7)

# Fecha inicial: hace una semana, a las 00:00:00 UTC
fecha_ini = una_semana_atras.strftime("%Y-%m-%dT00:00:00UTC")

# Fecha final: el día de hoy menos un día, a las 23:59:59 UTC
fecha_fin = (hoy - timedelta(days=1)).strftime("%Y-%m-%dT23:59:59UTC")

print(f"Fecha inicial: {fecha_ini}")
print(f"Fecha final: {fecha_fin}")

print(f"Obteniendo datos desde {fecha_ini} hasta {fecha_fin}")

# Estación fija
idema = "5790Y"






# PASO 3: Realizar las peticiones
todos_los_datos = []
metadatos = None

print(f"Realizando petición para la estación {idema} entre {fecha_ini} y {fecha_fin}")

# METADATOS
URL_BASE = "https://opendata.aemet.es/opendata"
PETICION_METADATOS = f"/api/valores/climatologicos/diarios/datos/fechaini/{fecha_ini}/fechafin/{fecha_fin}/estacion/{idema}"
respuesta_metadatos = requests.get(URL_BASE + PETICION_METADATOS, headers=headers)

if respuesta_metadatos.status_code == 200:
    try:
        metadatos = respuesta_metadatos.json()
        print("Metadatos obtenidos correctamente.")

        # Segunda consulta para los metadatos completos
        if "metadatos" in metadatos:
            metadatos_url = metadatos["metadatos"]
            respuesta_metadatos_completos = requests.get(metadatos_url)

            if respuesta_metadatos_completos.status_code == 200:
                metadatos = respuesta_metadatos_completos.json()
                print("Metadatos completos obtenidos.")
            else:
                print(f"Error al obtener los metadatos completos. Código: {respuesta_metadatos_completos.status_code}")
        else:
            print("No se encontró la clave 'metadatos' en la respuesta de la primera consulta.")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar los metadatos: {e}")
else:
    print(f"Error al obtener los metadatos. Código: {respuesta_metadatos.status_code}")
    sys.exit()

sleep(5)

# DATOS CLIMÁTICOS
PETICION = f"/api/valores/climatologicos/diarios/datos/fechaini/{fecha_ini}/fechafin/{fecha_fin}/estacion/{idema}"
respuesta = requests.get(URL_BASE + PETICION, headers=headers)

if respuesta.status_code == 200:
    try:
        data = respuesta.json()
        if "datos" in data:
            datos_url = data["datos"]
            print(f"Descargando datos desde: {datos_url}")

            respuesta_datos = requests.get(datos_url)

            try:
                datos_finales = json.loads(respuesta_datos.text)
                print("Datos climáticos obtenidos correctamente.")
                todos_los_datos.extend(datos_finales)
                sleep(5)
            except json.JSONDecodeError as e:
                print(f"Error al decodificar los datos JSON: {e}")
        else:
            print("No se encontró la clave 'datos' en la respuesta.")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar los datos JSON: {e}")
else:
    print(f"Error en la petición inicial: Código {respuesta.status_code}")




# PASO 4: Obtener el resumen de los datos hecho por GPT4all


model = GPT4All("mistral-7b-openorca.Q4_0.gguf")  # primer uso lo descarga
with model.chat_session() as session:
    response = session.generate("""Estos son los datos meteorológicos diarios de Sevilla durante la última semana:
                                    {datos}
                                    Haz un pequeño resumen del tiempo que ha hecho en Sevilla esta semana, de forma clara y natural.
                                    recuerda que son datos ya pasados.""")
    print(response)






# PASO 5 Leer el contenido del archivo de texto

# Convertir el texto a audio (MP3)
tts = gTTS(text=response, lang='es')  # 'es' para español
tts.save("resumen_semana.mp3")

# Reproducir el archivo MP3
os.system("start resumen_semana.mp3") 