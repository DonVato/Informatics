#!/usr/bin/env `python
# -*- encoding: utf-8 -*-
#Functions List

import feedparser
import re
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Top Ranked Journals of Chemistry
Table of All Possible RSS Feeds to choose from
"""
websiteLists = {"Journal of Biological Chemistry": "http://feeds.feedburner.com/jbc/SUcv", "Journal of American Chemical Society": "http://feeds.feedburner.com/acs/jacsat", "Journal of Agricultural and Food Chemistry": "http://feeds.feedburner.com/acs/jafcau", "Journal of Chemical and Engineering Data":"http://feeds.feedburner.com/acs/jceaax", 
"Journal of Chemical Education": "http://feeds.feedburner.com/acs/jceda8",
"Journal of Chemical Physics": "http://scitation.aip.org/rss/content/aip/journal/jcp/latestarticles;jsessionid=52cwl8qj3dt7.x-aip-live-01?fmt=rss", "Journal of Physical Chemistry A": "http://feeds.feedburner.com/acs/jpcafh",
"Journal of Applied Polymer Science": "http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1097-4628", "Langmuir": "http://feeds.feedburner.com/acs/langd5",
"Chemical Physics Letters": "http://www.journals.elsevier.com/chemical-physics-letters/rss/", "Chemical Communications": "http://feeds.rsc.org/rss/cc",
"Acta Crystallographica ":"http://journals.iucr.org/b/journalhomepage.html", 
"Journal of Chemical Information and Modeling": "http://feeds.feedburner.com/acs/jcisd8", "Journal of Chemical Theory and Computation": "http://feeds.feedburner.com/acs/jctcce",
"Journal of Medicinal Chemistry": "http://feeds.feedburner.com/acs/jmcmar", "Journal of Natural Products": "http://feeds.feedburner.com/acs/jnprdf", "The Journal of Organic Chemistry" :"http://feeds.feedburner.com/acs/joceah",
"Journal of Proteome Research":"http://feeds.feedburner.com/acs/jprobs","Organometallics":"http://feeds.feedburner.com/acs/orgnd7",
"Nano Letters": "http://feeds.feedburner.com/acs/nalefd"}

websiteLists1 = ["http://feeds.feedburner.com/acs/langd5","http://feeds.feedburner.com/acs/jprobs"]
""""""""""""""""""""""""""""""""""""""""""""""""""""""

def insertFeed(a):
	x = feedparser.parse(a)
	return x

''' 
Print through all the posts of the website
'''
def printALLPosts(a):
	for post in a.entries:
		print post.title + ":" + post.link + "\n"

def printListofJournals(a):
	for a in a:
		print a
''''''''''''''''''''''''''''''''''''''''''''''''
def returnListofTitles(a):
	dList = []
	for i in range(len(a)):
		b = a[i].title
		#b.encode("ascii","ignore")
		dList.append(b)
	return dList;

def returnListofAuthors(a):
	dList = []
	for i in range(len(a)):
		b = a[i].author
		#b.encode("ascii","ignore")
		dList.append(b)
	return dList;

def returnListofPubDate(a):
	dList = []
	for i in range(len(a)):
		b = a[i].published
		c = re.sub("\D", "", b)	
		d = c[2:6]
		dList.append(d)
	return dList;

############################################

def encodeList(a):
	dList = []
	for i in range(len(a)):
		b = a[i].encode('utf-8')
		dList.append(b)
	return dList;
#############################################
#MySQL Commands


def printMySQLResults(a):
	for row in a :
		print row[0] 
		print row[1]
		print row[2]
		print "\n"