#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

# UTILS
def create_row(factory):
	row = factory.new_tag('tr')
	td1 = factory.new_tag('td')
	td2 = factory.new_tag('td')
	td2['class'] = 'right'
	row.append(td1)
	row.append(td2)
	return row
def create_div(factory):
	table = factory.new_tag('table')
	table['class'] = 'table'
	div = factory.new_tag('div')
	div['class'] = 'table-responsive'
	div.append(table)
	return div
def append_clicker(table, temp):
	clicker = temp.new_tag('tr')
	clicker['class'] = 'clicker'
	table.append(clicker)
	return
def get_icon(temp):
	span = temp.new_tag('span')
	span['class'] = 'glyphicon glyphicon-chevron-left'
	return span
def name(src):
	from transliterate import translit, get_available_language_codes
	name = translit(src, 'ru', reversed=True).replace(' ', '_')
	new_name = name.replace(',', '').replace('.', '').replace(')', '').replace('(', '').replace(':', '').replace('\'', '')
	return new_name + '.html'
# END UTILS
# READ SRC FILE
with open(sys.argv[1]) as f:
    content = f.readlines()
lines = filter(None, [x.strip() for x in content])
# READ TEMPLATE FILE
with open('template.html') as f:
    template = f.read().replace('\n', '')
# DECLARE VARS
HEADER = BeautifulSoup('<div class="list-group" id="myUL"></div>', 'html.parser')
major = BeautifulSoup("", 'html.parser')
temp = BeautifulSoup("", 'html.parser')
append_to_temp = []
headers = []
count = 0
max = len(lines)
max = 0
i = 0
while i < (len(lines) - 2):
	# i is text
	tr = create_row(temp)
	tr.find_all('td')[0].string = lines[i]
	# next item analisys
	if lines[i+1].endswith('.') or lines[i+1].endswith('%'):
		# INFO!!!
		# PRICE
		tr.find_all('td')[1].string = lines[i+1]
		tr.find_all('td')[1]['class'] = 'right'
		tr['style'] = 'display: none;'
		# APPEND TO LIST
		append_to_temp.append(tr)
		# SET I
		i += 2
	else:
		# HEADER!!!
		count += 1
		if count == 2:
			# PACK !!! ADD CLICKER !!!
			div = create_div(temp)
			for row in append_to_temp:
				div.table.append(row)
			# BUILD TEMPLATE
			page = BeautifulSoup(template, 'html.parser')
			page.find_all('div', class_='info-column col-md-8')[0].append(div)
			file_n  = name(tr.find_all('td')[0].string)
			path = 'services/' + file_n
			# BUILD TEMPLATE
			# WRAP STRING TO A
			a = HEADER.new_tag('a')
			a['href'] = path
			a.string = append_to_temp[0].find_all('td')[0].string
			a['class'] = 'list-group-item'
			headers.append(a)
			append_to_temp[0].find_all('td')[0].string.wrap(a)
			# END BUILD TEMPLATE
			major.append(div)
			append_to_temp = []
			count = 1
		# PROCESS HEADER
		tr.find_all('td')[0].string = lines[i]
		tr.find_all('td')[0].string.wrap(temp.new_tag('h4'))
		tr.find_all('td')[1].append(get_icon(temp))
		tr['class'] = 'clicker'
		# APPEND TO LIST
		append_to_temp.append(tr)
		# SET I
		i += 1
# WRITE OUT THE RESULT
for header in headers:
	text = header.get_text("|")
	new = text.split("|")[0]
	header.string = new
	HEADER.div.append(header)
with open('out_v2.txt', 'w+') as out:
	out.write(HEADER.prettify(formatter='minimal').encode('utf8'))