# Written for GD Demon Ladder
# by RFMX (c) 2021

# This script will return level data after you inputted the ID into levels.html
# I wrote this on repl.it so I did not bother on line length lulz
# Comments refer to the previous line except for headers, marked with *

# Basic flow:
# 1) make a HTTP request (Ajax call) to get data in column E of the list, which is a list of IDs of demons
# 2) find where the desired ID is through the index() function and save that into a variable
# 3) make a HTTP request again to get data in the row the demon is in
# 4) extract data by utilising the arrangement of the data in the row and print it into the table

# ** Setup **

# * Import libraries *
from browser import document, ajax, html
import json

# * Changing variables *
key = 'AIzaSyC5EjLYGlY6W6zfkcQiQ6nK74zk_7yEjHk' # API key
default_demon = '69274427' # Demon for no input, usually weekly

def on_complete(req):	
	# ** extract for ID **
	try: id_search = str(document.query['id']) # extract ID
	except: id_search = default_demon # if ID parameter does not exist

	# * Load ID list *
	r_json = json.loads(req.text) # convert to json
	r_json = r_json['values'] # extract the values section

	# r_json is now an array of IDs with index that is OFF BY ONE compared to row number

	# ** search for the specific ID **
	id_array = []
	id_array.append(id_search)
	try:
		demon_no = r_json.index(id_array)
	except: demon_no = -1
	row_no = demon_no + 1

	# ** URL setup **
	row_select = "'The List'!" + str(row_no) + ":" + str(row_no)
	apiurl = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/" + row_select + "?key=" + key

	# ** Ajax call setup **
	if demon_no != -1:
		call = ajax.ajax()
		call.bind('complete', on_complete2)
		call.open('GET', apiurl, True)
		call.send()
	else:
		document['levelname'] <= 'There is no demon with the ID ' + str(document.query['id']) + '!'

# ** the on_complete function **
# the on_complete function executes after all the code is executed, which is a problem because I need to extract data from the Ajax call
# ===OBSOLETE=== thankfully I only need to extract web data once from the json file and once from the web so I am throwing a lot of stuff into the on_complete function
# I have migrated into having two Ajax call in a single script because this removes the need for me to constantly update the file

def on_complete2(req):
	r_json = json.loads(req.text) # converts to JSON
	r_json = r_json['values'] # extracts values
	r_json = r_json[0] # get into the array
	# sheets API always sort by ROWS as the major dimension

	# ** prints stuff on screen **
	# index is based on column oreder
	document['levelname'] <= r_json[0] + ' ('
	gdbrowser_url = 'https://gdbrowser.com/' + r_json[4]
	document['levelname'] <= html.A(r_json[4], href=gdbrowser_url, target="_blank")
	document['levelname'] <= ')'
	document['levelcreator'] <= r_json[1]
	document['levelsong'] <= r_json[2]
	document['leveldiff'] <= r_json[3]
	if r_json[5] != "unrated":
		document['leveltier'] <= 'Tier ' + r_json[5] + ' (' + r_json[6] + ' corr to 2 d.p.)'
		# document['levelratings'] <= 'Submitted ratings:'
		# document['levelratings'] <= html.BR()
		i = 7
		try:
			while r_json[i] != '':
				levelratings = ''
				levelratings = ''.join([levelratings,'- Tier ',r_json[i]])
				i = i + 1
				levelratings = ''.join([levelratings,' by ',r_json[i]])
				i = i + 1
				document['levelratings'] <= levelratings
				document['levelratings'] <= html.BR()
		except: pass
	else: document['leveltier'] <= 'Not rated with a tier (yet)'

# ** Ajax call setup **
firstcallurl = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'The List'!E:E?key=" + key

call = ajax.ajax()
call.bind('complete', on_complete)
call.open('GET', firstcallurl, True)
call.send()

