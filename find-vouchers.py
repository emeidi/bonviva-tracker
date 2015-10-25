#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import sys
import os
import io

import subprocess

import re

import json

from operator import itemgetter

verbose=False

scriptRoot=os.path.dirname(os.path.realpath(__file__))
basePath=scriptRoot + "/cache"

debugPath="./debug.txt"
debugFile = io.open(debugPath,'w',encoding='utf-8')

def d(msg):
	debugFile.write(unicode(msg) + "\n")
	
	if verbose == False:
		return
	
	print msg

if not os.path.isdir(basePath):
	print "ERROR: Directory '" + basePath + "' does not exist. Please run mirror.sh and parse.py first to mirror and parse the Bonviva web site."
	sys.exit(1)

# Get master JSONs in cache dir
files = []
for filename in os.listdir(basePath):
	if '.json' not in filename:
		d(filename + ' is not a JSON file. Skipping.')
		continue
		
	d(filename + ' is a JSON file. Adding it to the list.')
		
	files.append(os.path.join(basePath, filename))

if len(files) < 1:
	print "ERROR: No .json files found in directory '" + basePath + "'. Please run mirror.sh and parse.py first to mirror and parse the Bonviva web site."
	sys.exit(1)

filesSorted = sorted(files, reverse=True)
#print filesSorted
#sys.exit(0)

mostRecentJSONDumpPath = filesSorted[0]

d('Reading ' + mostRecentJSONDumpPath + ' ...')
d('')

f = open(mostRecentJSONDumpPath)
jsonRaw = f.read()
f.close

items = json.loads(jsonRaw)

check = []
list = []
for item in items:
	pattern = "CHF ([0-9]+)" # TODO: a more flexible approach
	match = re.search(pattern,item['item'])
	
	if not match:
		d(str(item['id']) + " with title '" + item['item'] + "' did not match pattern " + pattern + ". Skipping.")
		continue
		#return False
	
	if item['id'] in check:
		d(str(item['id']) + " is a duplicate. Skipping.")
		continue
	
	check.append(item['id'])
	
	chfvalue = int(match.group(1))
	d("Item has a real price of " + str(chfvalue) + " CHF")
	
	d("Item costs " + str(item['points']) + " Bonviva Points")
	
	pointvalue = chfvalue/item['points']
	d("1 Bonviva Point is worth " + str(pointvalue) + " CHF")
	
	kpointvalue = pointvalue * 1000;
	
	d("1000 Bonviva Points are worth " + str(kpointvalue) + " CHF")
	
	tmp = {
		'id': item['id'],
		'item': item['item'],
		'description': item['description'],
		'points': item['points'],
		'price': chfvalue,
		'pointvalue': pointvalue,
		'kpointvalue': kpointvalue
	}
	
	#list[item['id']] = tmp
	list.append(tmp)

#print list

itemsSorted = sorted(list, key=itemgetter('pointvalue'), reverse=True)

for item in itemsSorted:
	decimal_format = "{:.2f}"
	kpointvaluePretty = round(item['kpointvalue'],2)
	kpointvaluePretty = decimal_format.format(kpointvaluePretty)
	
	numSpacer = 55 - len(item['item'])
	spacer = '.' * numSpacer
	print '[' + str(item['id']) + '] ' + item['item'] + ' ' + spacer + ' ' + str(kpointvaluePretty)

sys.exit(0)