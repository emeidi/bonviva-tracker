#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import io

import time

import re

import json

from BeautifulSoup import BeautifulSoup

verbose=False

scriptRoot=os.path.dirname(os.path.realpath(__file__))
basePath=scriptRoot + "/cache"

debugPath="./debug.txt"
debugFile = open(debugPath,'w')

def d(msg):
	debugFile.write(msg + "\n")
	
	if verbose == False:
		return
	
	print msg

def parseHtml(file=None):
	if file is None:
		return False
	
	id = int(getIdFromPath(file))
	#url = "https://rewards.credit-suisse.com/cs/rewards/p/d/commodityRewardDetails.do?source=SP&menuId=n0&id=" + str(id)
	
	date = getDateFromPath(file)
	
	# Read HTML
	f = open(file)
	htmlRaw = f.read()
	f.close
	
	html = BeautifulSoup(htmlRaw)
	
	# <meta property="og:url" content="https://rewards.credit-suisse.com/cs/rewards/p/d/commodityRewardDetails.do?source=SP&menuId=n0&id=31"/>
	# <meta property="og:title" content="SAMSONITE Digitale Gepäckwaage"/>
	# <meta property="og:description" content="Leicht, kompakt - und trotzdem kraftvoll: der Akku-Schrauber von BOSCH für universelle Schraubanwendungen. Durch das ergonomische Design mit Softgrip liegt das Gerät perfekt in der Hand, neueste Akkutechnik sorgt für extralange Laufzeiten."/>
	
	propertiesHelper = {
		'url': 'og:url',
		'title': 'og:title',
		'description': 'og:description'
	}
	
	properties = {}
	for var, property in propertiesHelper.iteritems(): # .iteritems() in Python 2.x
		meta = html.find('meta', {"property": property})
		
		if not meta:
			d("Could not find " + property + ". Skipping.")
			return False
		
		if not meta['content']:
			d("meta " + property + " found, but no attribute 'content' present. Skipping.")
			return False
		
		properties[var] = meta['content']
	
	# Find points
	span = html.find('span', {"class" : "points"})
	#pointsRaw = span.contents
	
	if not span:
		print "No points for ID " + str(id) + ". Skipping."
		return False
	
	pointsRaw = ''.join(span.contents).strip()
	
	pattern = "([0-9\']+) Punkte"
	match = re.search(pattern,pointsRaw)
	
	if not match:
		return False
	
	pointsDirty = match.group(1)
	points = int(pointsDirty.replace("'",''))
	
	# Fill in data
	data = {
		'id': id,
		'url': properties['url'],
		'item': properties['title'],
		'description': properties['description'],
		'points': points,
		'date': date
	}
	
	return data

def getIdFromPath(path=None):
	if path is None:
		return False
	
	pathParts = path.split('/')
	
	return pathParts[-2] # gets second last atom

def getDateFromPath(path=None):
	if file is None:
		return False
	
	pathParts = path.split('/')
	
	filename = pathParts[-1] # gets last atom
	
	return filename.replace('.html','')

def dumpObjToJSON(obj=None,path=None):
	if obj is None:
		d("obj=None")
		return false
	
	if path is None:
		d("path=None")
		return false
	
	data = unicode(json.dumps(obj, ensure_ascii=False))
	
	d("Writing " + str(len(data)) + " bytes to '" + path + "' ...")
	f = io.open(path,'w',encoding='utf-8')
	f.write(data)
	f.close
	
	return True

dirs = []
for dirname, dirnames, filenames in os.walk(basePath):
	for subdirname in dirnames:
		dirs.append(os.path.join(dirname, subdirname))

#print dirs
d(str(len(dirs)) + " directories to traverse")

# Traverse directories

master = []
for dir in dirs:
	d("Looking into '" + dir + "' ...")
	
	for dirname, dirnames, filenames in os.walk(dir):
		for filename in filenames:
			path = dir + '/' + filename
			
			if '.html' not in filename:
				d("'" + filename + "' is not a HTML file. Skipping.")
				continue
			
			d("Parsing file " + path + " ...")
			data = parseHtml(path)
			
			if data is False:
				continue
			
			print ""
			print data
			
			# Dump as JSON
			dumpPath = dir + '/' + filename.replace('.html','.json')
			res = dumpObjToJSON(data,dumpPath)
			
			if res != True:
				print "dumpObjToJSON() did not return True. Please investigate. Aborting."
				sys.exit(1)
			
			# Add to master
			master.append(data)

today = time.strftime('%Y-%m-%d') 
dumpPath = basePath + '/' + today + '.json'
res = dumpObjToJSON(master,dumpPath)

d("Done.")
sys.exit(0)