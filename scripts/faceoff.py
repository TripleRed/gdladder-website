# Written for GD Demon Ladder
# by RFMX (c) 2021

# unlike other scripts here, this is directly written on replit
# because I am fed with translating the request package into Ajax calls

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
import os, random, json
from browser import document, ajax, html

# ** Variables that needs constant updates **
key = 'AIzaSyC5EjLYGlY6W6zfkcQiQ6nK74zk_7yEjHk'

# ** on_complete function **
def on_complete(req):	
	document['testping'] <= "ping"
	document['faceoffresponse'] <= req.text

# ** test PUT Ajax call **

url = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'Demon Face-off'!A1:C1?majorDimension=ROWS&key=" + key
call = ajax.ajax()
call.bind('complete', on_complete)
call.open('PUT', url, True)
call.send({"range":"A1:A3","majorDimension":"ROWS","values":["a","b","c"]})