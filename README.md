# API-LLM-gTTS-homemade-alexa-
Using AEMET API combined with  local LLM to hear a resume of local wheater 


#  INTRODUCTION

On this Python script we will use the API from AEMET (Agencia Estatal de Meterorologia, spanish wheater service) to obtain weather data from the last week in a Spanish city.
We will pass this data to a local LLM and we will transform the answer in to a MP3 to rerpoduce it on the local PC audio.
This script is made and tested using windows. I'm not sure if there could be some problems for linux users



#   FILES

Main file is "archivo_completo".  This file contains the full script and can be used alone. 
It's the only thing that you need if you want to try this script


For those who want to adapt this script i have included 3 aditionals files, one for every "part" of the main file.


-FIRST ONE, "datos_semana".
It uses the AEMET API to retrieve the wheather data of the last week in Seville. After that it will save those data in a JSON file.  
The main file will don't save any data, so if you want to save the data for another thing you can simply run this file.
If you want to use other date, or other city modify this part of the script is very easy.  
I have another repositorie specifically for AEMET API here:  https://github.com/fenris123/USING-AEMET-API-TO-OBTAIN-WEATHER-DATA-FROM-SPANISH-CITIES



-SECOND ONE, "promt_GPT4all"

This script will use the file created by "datoos_semana" and ask the LLM to make a resume about them. After that, it will save the answer in a TXT file.
To keep the things simple on this script we use the default LLM installed by the library gpt4all:  "mistral-7b-openorca.Q4_0.gguf"
We will discuse about that  later.
Remember that the main file will not save any file, nor use it.  It will take the data directly. 
This 3  "split" files write and read files because i wanted to separate the main parts, for those who want to experiment with them.



-THIRD ONE, "transformacion_mp3"

This files just take the .txt file, translate it into a mp3 and launches it.
(Again, the main file just don't need any .MP3 file. It will take the LLM response directly without saving it)
You can use this file to read any .txt file that you want simply changing the route.



-ENVIROMENT FILE, "tokens.env"

Used to keep your AEMET token private and don't include it in the code.
Look the "Using AEMET API" ahead.








#  LIBRARIES

json

os

requests

sys

dotenv

datetime

time

gpt4all

gtts


#  REQUIREMENTS TO USE THE AEMET API

As I said before, i have another repository about AEMET API here:  https://github.com/fenris123/USING-AEMET-API-TO-OBTAIN-WEATHER-DATA-FROM-SPANISH-CITIES
If you don't want to read it, here is the basic things.

To use AEMET API, you need a token.  You can request one here:   https://opendata.aemet.es/centrodedescargas/altaUsuario?
After that, open the "tokens.env" file (is just a .txt with another "name") and copy your token there.

Be sure that the route to the token.env file is the used on the script.  
Look for this line in the code: load_dotenv("C:/espaciopython/enviroments/tokens.env"). 
Put your file in that carpet, or simply change the line. (Be careful with the "/" and "\")) 




#  LLM.

To maintain the things simple, we have used the LLM installed by default by gtts: mistral-7b-openorca.Q4_0.gguf
It will be dowloaded automatically in the first time that you use the code.


BE CAREFULL:  IT WIL NEED 4 GIGAS OF FREE SPACE.
THIS IS WHAT HAPPENS ON 21/04/2025.
If you are reading this after that day, i hope that they will not change it.


On my PC, with a intel 11400, 16GB of RAM and a rtx 6600, the main file needs about 50 seconds since you launch the script until it reproduces the answer.
You can change the LLM to obtain faster answers. 
You only need to find where is the file "mistral-7b-openorca.Q4_0.gguf" in your PC, and donwload other LLM on that directory and change the line model = GPT4All("mistral-7b-openorca.Q4_0.gguf") with the new name.
The main problem is that faster answers usualy are worse.


Using Llama-3.2-3B-GGUF.Q8_0.gguf i.e.  only requires 19 seconds, BUT using the same pront the answer is almost a telegram, with no details at all. 
mistral-7b-openorca.Q4_0.gguf on the other side gives a richer and more complete answer


If you can try another LLM, do it: it's very fun!


#  FINAL THOUGHS.

To me this proyect is finished and closed. I hope that you find al this as interesting as i did.
I will use all of this as a base for another things for sure, but i'm not going to ad anything more to this repository.
So now it's your turn to try it and change it!


