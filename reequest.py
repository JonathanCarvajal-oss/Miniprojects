#Modulo request, hace peticinoes, llamadas a API, etc
#get, delete, 
import requests

#Llamada a la api que es unaURL que se usa para aps
respuesta = requests.get('https://www.facebook.com/reel/1029932945370211')

data = respuesta.json()
print(data)

#jugar con la api para que imprima una parte con lo que le pido
print([A][B])