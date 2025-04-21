# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 13:17:17 2025

@author: fenris123
"""

from gtts import gTTS
import os

# Leer el contenido del archivo de texto
with open("resumen_semana.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Convertir el texto a audio (MP3)
tts = gTTS(text=texto, lang='es')  # 'es' para español
tts.save("resumen_semana.mp3")

# Reproducir el archivo MP3
os.system("start resumen_semana.mp3")  