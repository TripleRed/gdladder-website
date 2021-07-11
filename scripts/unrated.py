# Written for GD Demon Ladder
# by RFMX (c) 2021

# This script is modified from filters.py to show all unrated levels
# Comments refer to the previous line except for headers, marked with *

# ** Setup **
from browser import document, ajax, html
import json

# ** Variables that needs constant updates **
# thank you Tom Scott to remind me of future compatibility
key = 'AIzaSyC5EjLYGlY6W6zfkcQiQ6nK74zk_7yEjHk'
filterno = 7
colno = "4"
referencelist = [""]

def ceiling(number):
	k = 0
	while True:
		if float(k) >= float(number): return k
		else: k += 1
# ceiling function: only works for positive numbers, but that is enough, I am too lazy to port the library

def on_complete(req):
	r_json = json.loads(req.text)
	r_json = r_json['values']

	# ** Filter for unrated levels **
	# * setup list *
	result = []
	i = 1
	while i < len(r_json[4]):
		result.append(i)
		i += 1

	# * filter for unrated demons *
	list = []
	try:
		while True:
			check_list = result.pop(0)
			check_try = str(r_json[5][check_list])
			if check_try == "unrated": list.append(check_list) # comparison check
	except: pass
	try:
		while True:
			result.append(list.pop(0))
	except: pass

	# ** Listing results **

	# * setup *
	table = html.TABLE('', id='unratedtable')

	recent = -1

	try:
		i = -10 * int(page)
	except: i = 0
	noresults = True

	totalresults = len(result)
	totalpages = ceiling(totalresults / 10)

	# * first row *

	table <= html.TR(html.TH("Name", Class="filtersth", colspan="2") + html.TH("Creator", Class="filtersth", colspan="2") + html.TH("ID", Class="filtersth", colspan="2"))

	# * item rows *

	try:
		while True:
			resultpop = result.pop(recent)
			entryname = (r_json[0][resultpop])
			entrycreator = (r_json[1][resultpop])
			id_url = "https://gdladder.tk/levels.html?id=" + r_json[4][resultpop]
			entryid = html.A(r_json[4][resultpop], href=id_url)
			table <= html.TR(html.TD(entryname, Class="filterstd", colspan="2") + html.TD(entrycreator, Class="filterstd", colspan="2") + html.TD(entryid, Class="filterstd", colspan="2"))
			i += 1
			noresults = False
	except: pass
	document['unratedresults'] <= table

	if noresults:
		document['unratedstats'] <= 'No unrated demons, yay!'
	else:
		document['unratedstats'] <= str(totalresults) + ' levels unrated'

# ** URL request **

url = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'The List'!A:G?majorDimension=COLUMNS&key=" + key
call = ajax.ajax()
call.bind('complete', on_complete)
call.open('GET', url, True)
call.send()
