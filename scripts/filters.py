# Written for GD Demon Ladder
# by RFMX (c) 2021

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
from browser import document, ajax, html
import json, random

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

def changeWord(word):
    for letter in word:
        if letter == "+":
            word = word.replace(letter," ")
    return word
# thanks to StackOverflow: first written by Aei then modified by JoelWilson

def on_complete(req):
	r_json = json.loads(req.text)
	r_json = r_json['values']

	errorcount = 0
	# ** 'Ask' for filters **
	try: tiermin = str(document.query['tiermin'])
	except: 
		tiermin = ''
		errorcount += 1

	try: tiermax = str(document.query['tiermax'])
	except:
		tiermax = ''
		errorcount += 1

	try: official_diff = str(document.query['official_diff'])
	except:
		official_diff = ''
		errorcount += 1

	try:
		name = str(document.query['name'])
		name = changeWord(name)
	except:
		name = ''
		errorcount += 1

	try:
		if str(document.query['sort']) == 'recent':
			sort = "recent"
			recent = 1
		elif str(document.query['sort']) == 'byid':
			sort = "byid"
			recent = 0
		elif str(document.query['sort']) == 'random':
			sort = "random"
			recent = 0
		else:
			raise Exception("Unknown parameter")
	except:
		sort = "byid"
		recent = 0
		errorcount += 1

	try: page = str(document.query['page'])
	except:
		page = 0
		errorcount += 1

	try:
		if str(document.query['reference']) == 'on':
			reference = 1
		else: reference = 0
	except:
		reference = 0
		errorcount += 1
	
	if errorcount == filterno:
		return

	# * querystring construction *
	querystring = "?"
	if tiermin != '':
		querystring += ("tiermin=" + tiermin + "&")
	if tiermax != '':
		querystring += ("tiermax=" + tiermax + "&")
	if official_diff != '':
		querystring += ("official_diff=" + official_diff + "&")
	if name != '':
		querystring += ("name=" + name + "&")
	if sort != '':
		querystring += ("sort=" + sort + "&")
	if reference == 1:
		querystring += ("reference=on&")
	querystring = querystring[0:-1]
	if querystring == "": querystring = "?"

	# ** Filter for levels **
	# * setup list *
	result = []
	i = 1
	while i < len(r_json[4]):
		result.append(i)
		i += 1

	# * Minimum tier *
	if tiermin != '':
		try:
			tiermin = int(tiermin)
		except: tiermin = float(tiermin)
		list = []
		try:
			while True:
				check_list = result.pop(0)
				if isinstance(tiermin, int):
					try:
						check_try = int(r_json[5][check_list])
					except: check_try = 0
				elif isinstance(tiermin, float):
					try:
						check_try = float(r_json[6][check_list])
					except: check_try = 0.0
				if tiermin <= check_try: list.append(check_list) # comparison check
		except: pass
		try:
			while True:
				result.append(list.pop(0))
		except: pass

	# * Maximum tier *
	if tiermax != '':
		try:
			tiermax = int(tiermax)
		except: tiermax = float(tiermax)
		list = []
		try:
			while True:
				check_list = result.pop(0)
				if isinstance(tiermax, int):
					try:
						check_try = int(r_json[5][check_list])
					except: check_try = 0
				elif isinstance(tiermax, float):
					try:
						check_try = float(r_json[6][check_list])
					except: check_try = 0.0
				if tiermax >= check_try: list.append(check_list) # comparison check
		except: pass
		try:
			while True:
				result.append(list.pop(0))
		except: pass

	# * Official difficulty *
	if official_diff != '':
		official_diff = int(official_diff)
		list = []
		try:
			while True:
				check_list = result.pop(0)
				try:
					check_try = (r_json[3][check_list])
					if check_try == 'Official Level':
						check_try = 0
					elif check_try == 'Easy Demon':
						check_try = 1
					elif check_try == 'Medium Demon':
						check_try = 2
					elif check_try == 'Hard Demon':
						check_try = 3
					elif check_try == 'Insane Demon':
						check_try = 4
					elif check_try == 'Extreme Demon':
						check_try = 5
				except: check_try = -1
				if official_diff == check_try: list.append(check_list) # comparison check
		except: pass
		try:
			while True:
				result.append(list.pop(0))
		except: pass

	# * Level name *
	if name != '':
		name = name.lower()
		list = []
		try:
			while True:
				check_list = result.pop(0)
				try:
					check_try = r_json[0][check_list].lower()
				except: check_try = ''
				if name in check_try: list.append(check_list) # comparison check
		except: pass
		try:
			while True:
				result.append(list.pop(0))
		except: pass

	# ** Listing results **

	# * shuffle list if needed *
	if sort == "random": random.shuffle(result)

	# * setup *
	table = html.TABLE('', id='centertable')

	try:
		recent = -1 * int(recent)
	except: recent = 0

	try:
		i = -10 * int(page)
	except: i = 0
	noresults = True

	totalresults = len(result)
	totalpages = ceiling(totalresults / 10)

	# * first row *

	table <= html.TR(html.TH("Name", Class="filtersth", colspan="2") + html.TH("Creator", Class="filtersth", colspan="2") + html.TH("ID", Class="filtersth", colspan="2") + html.TH("Tier", Class="filtersth", colspan="2"))

	# * item rows *

	try:
		while True:
			resultpop = result.pop(recent)
			if i >= 10:
				break
			elif i >= 0:
				noresults = False
				entryname = (r_json[0][resultpop])
				entrycreator = (r_json[1][resultpop])
				id_url = "https://gdladder.tk/levels.html?id=" + r_json[4][resultpop]
				entryid = html.A(r_json[4][resultpop], href=id_url)
				if str(r_json[5][resultpop]) == "unrated": entrytier = "N/A"
				else: entrytier = str(r_json[5][resultpop]) + " (" + str(r_json[6][resultpop]) + ")"
				table <= html.TR(html.TD(entryname, Class="filterstd", colspan="2") + html.TD(entrycreator, Class="filterstd", colspan="2") + html.TD(entryid, Class="filterstd", colspan="2") + html.TD(entrytier, Class="filterstd", colspan="2"))
			i += 1
	except: pass
	document['filtersresults'] <= table

	# * last row *
	lastpage = int(page) - 1
	lastpageurl = "filters.html" + querystring + "&page=" + str(lastpage)
	nextpage = int(page) + 1
	nextpageurl = "filters.html" + querystring + "&page=" + str(nextpage)

	if (int(page) != 0) and (sort != "random"): lastpage = html.A(html.BUTTON("Last page", Class="fillcell"), href=lastpageurl)
	else: lastpage = ""

	if (int(page) != (int(totalpages) - 1)) and (sort != "random"): nextpage = html.A(html.BUTTON("Next page", Class="fillcell"), href=nextpageurl)
	else: nextpage = ""

	table <= html.TR(html.TD(lastpage, Class="filtersth", colspan=colno) + html.TD(nextpage, Class="filtersth", colspan=colno))

	if noresults:
		document['searchstats'] <= 'No results.'
	elif sort == "random":
		document['searchstats'] <= str(totalresults) + ' levels found but only 10 random results are shown.'
	else:
		document['searchstats'] <= str(totalresults) + ' levels found shown in ' + str(totalpages) + ' pages'

# ** URL request **

url = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'The List'!A:G?majorDimension=COLUMNS&key=" + key
call = ajax.ajax()
call.bind('complete', on_complete)
call.open('GET', url, True)
call.send()
