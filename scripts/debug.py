# Written for GD Demon Ladder
# by RFMX (c) 2021

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
from browser import document, ajax, html
import json, random

# ** URL request **

url = "https://discord.com/api/webhooks/848784394792599592/0OOZOeCsuNjJWu2DqhSnlOh1LVS-L8BT3ubD1HsjnuY4N_9Xmbx8Qs5OhvvbotJlAISl"
call = ajax.ajax()
call.open('POST', url, True)
call.send({'content':'testing if this is working'})