# Written for GD Demon Ladder
# by RFMX (c) 2021

# Comments refer to the previous line except for headers, marked with *

from browser import document, ajax
import json

# ** Setup **

key = 'AIzaSyCOqFj77mZRIjnZUO4TS0GLwC-zQiduyqE'
apiurl = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'The List'!E:E?key=" + key

document['test'].text = document.query['id']

#response = url_request("'The List'!E:E")



"""
def url_request(a1notation):
    apiurl = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/" + a1notation + "?key=" + key
    request(apiurl) # HTTP request
    r = res
    r = r['values']
    return r
""" 

"""
# ** extract for ID **
try: id_search = str(document.query['id'])
except: id_search = '1'

# ** JSON shenanigans **
# * search for the specific ID *
r_json = url_request("'The List'!E:E")
demon_no = -1
id_array = []
id_array.append(id_search)
try:
    demon_no = r_json.index(id_array)
except: pass
row_no = demon_no + 1
row_select = "'The List'!" + str(row_no) + ":" + str(row_no)
r_json = url_request(row_select)
r_json = r_json[0]

# * prints stuff on screen *
document['levelname'] <= r_json[0] + ' (' + r_json[4] + ')'
document['levelcreator'] <= 'created by ' + r_json[1]
document['levelsong'] <= 'Song: ' + r_json[2]
document['leveldiff'] <= r_json[3] + ' in-game'
if r_json[5] != "#DIV/0!":
    document['leveltier'] <= 'Rated as Tier ' + r_json[5] + ' (' + r_json[6] + ' corr to 2 d.p.)'
    levelratings = 'Submitted ratings:\n'
    i = 7
    try:
        while r_json[i] != '':
            levelratings = ''.join([levelratings,'- Tier ',r_json[i]])
            i += 1
            levelratings = ''.join(levelratings,' by ' + r_json[i])
            i += 1
            levelratings = ''.join(levelratings,'\n')
    except: pass
else: pass
"""