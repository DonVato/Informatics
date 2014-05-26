#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
'''
import feedparser
import MySQLdb 
from chemparser_funcs import*


'''
'''
'''
Python Stuff
'''

printListofJournals(websiteLists);

print "\nEnter Journal you want to be searched"
input = raw_input()
d = insertFeed(websiteLists[input])




'''
'''
'''
SQL STUFF
'''
print "\nuser, and password"
#x=raw_input()
y=raw_input()
z=raw_input()
#db1 = MySQLdb.connect(host="localhost",user= ,passwd="")
db1 = MySQLdb.connect(host = 'localhost',user = y,passwd = z)
cursor = db1.cursor()

cursor.execute('use test')
cursor.execute('DROP TABLE IF EXISTS `feed4dayz`;')
cursor.execute('CREATE TABLE `feed4dayz` (Author varchar(255),Title varchar(5000), Published varchar(25), FULLTEXT (Author,Title)) ENGINE=MyISAM;')

'''
for i in range(len(d.entries)):
	print d.entries[i].title
'''
titles = returnListofTitles(d.entries)
authors = returnListofAuthors(d.entries)
pubDate = returnListofPubDate(d.entries)


titles1 = encodeList(titles)
authors1 = encodeList(authors)


for  x in range(len(authors1)):
	cursor.execute('INSERT INTO feed4dayz(Author,Title,Published) VALUES(%s,%s,%s)',(authors1[x], titles1[x],pubDate[x])) 

#########################################################
#MYSQL Ranking Commands
print "How would you Like to Rank This Data"
print "\n a: Author\n b: Title\n c: Published"

chosen = raw_input()

if chosen is 'a':
	print "Type Author's First and/or Last Name	"
	input = raw_input()
	cursor.execute('SELECT * FROM feed4dayz where MATCH (Author) AGAINST (%s IN BOOLEAN MODE)',input) 
	print ""
if chosen is 'b':
	print "Papers will be presented descendingly based on frequency of keyword"
	print "Type Keyword"
	input = raw_input()
	cursor.execute('SELECT * FROM feed4dayz where MATCH (Title) AGAINST (%s IN BOOLEAN MODE) ORDER BY COUNT(Title)' ,input) 
	print ""
if chosen is "c":
	print "\nAscending or Descending?\na:ASC\nb:DESC"
	input = raw_input()
	if input is'a':
		cursor.execute('SELECT * FROM feed4dayz ORDER BY Published ASC')
	if input is 'b':
		cursor.execute('SELECT * FROM feed4dayz ORDER BY Published DESC')
	print ""




#########################################################
data = cursor.fetchall()

printMySQLResults(data)

db1.commit()



#printALLPosts(d);


'''FINAL NOTE TO ME 
You might have to aggregate the results then put all of 
results with the title and author and published 
in a list using a for loop
''' 