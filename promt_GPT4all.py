# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 12:37:48 2025

@author: fenris123
"""
from gpt4all import GPT4All
import json

with open(r"C:\espaciopython\CODIGOS UTILES\Chat-gpt\datos_semana.json", "r", encoding="utf-8") as f:
    datos = json.load(f)




model = GPT4All("mistral-7b-openorca.Q4_0.gguf")  # primer uso lo descarga
with model.chat_session() as session:
    response = session.generate("""Estos son los datos meteorológicos diarios de Sevilla durante la última semana:
                                    {datos}
                                    Haz un pequeño resumen del tiempo que ha hecho en Sevilla esta semana, de forma clara y natural.""")
    print(response)

with open("resumen_semana.txt", "w", encoding="utf-8") as f:
    f.write(response)