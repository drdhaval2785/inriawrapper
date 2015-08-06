#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
from bs4 import BeautifulSoup
import urllib2
import datetime
import time
import re

def timestamp():
	print datetime.datetime.now()

#print "code started at ",
#timestamp()


# function 's' for generating 'subanta'
""" The input format should be word.gender.case.vacana format. 
'gender' takes 'm'/'f'/'n'/'a' for musculine, feminine, neuter and any gender
'case' takes '1'/'2'/'3'/'4'/'5'/'6'/'7'/'0' for nominative/accusative/instrumental/dative/ablative/genitive/locative and sambodhana respectively.
'vacana' takes '1'/'2'/'3' for ekavacana, dvivacana and bahuvacana respectively
"""
def s(text):
	input = text.split('.')
	word = input[0]
	if input[1] == "m":
		gender = "Mas"
	elif input[1] == "f":
		gender = "Fem"
	elif input[1] == "n":
		gender = "Neu"
	elif input[1] == "a":
		gender = "Any"
	vibhaktinumber = input[2] + "." + input[3]
	url = "http://sanskrit.inria.fr/cgi-bin/SKT/sktdeclin?lex=MW&q=" + word + "&t=SL&g=" + gender + "&font=deva"
	vibhaktilist = ['1.1', '1.2', '1.3', '0.1', '0.2', '0.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3', '4.1', '4.2', '4.3', '5.1', '5.2', '5.3', '6.1', '6.2', '6.3', '7.1', '7.2', '7.3']
	numlist = [5,6,7,9,10,11,13,14,15,17,18,19,21,22,23,25,26,27,29,30,31,33,34,35]
	vinum = range(23)
	response = urllib2.urlopen(url)
	#print "webpage downloaded at ",
	#timestamp()
	html_doc = response.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	#print "soup made at ",
	#timestamp()
	vibh = []
	table = soup.find("table", { "class" : "inflexion" })
	for row in table.findAll("tr"):
		cells = row.findAll("th")
		for cell in cells:
			vibh.append(cell.text)
	
	return vibh[numlist[vibhaktilist.index(vibhaktinumber)]]
	
#print s('asmad.a.3.2')
#print "subanta form culled out at ",
#timestamp()

# function selecttable to select appropriate table for verb data scrapping.
# text in verb.gana.pada.lakara.vacya.purusa.vacana format.
def selectlakara(text):
	input = text.split('.')
	verb = input[0]
	gana = input[1]
	pada = input[2]
	lakara = input[3]
	vacya = input[4]
	purusa = input[5]
	vacana = input[6]
	lakaralist = ['लट्', 'लङ्', 'विधिलिङ्', 'लोट्', 'लृट्', 'लृङ्', 'लुट्', 'लिट्', 'लुङ्', 'आगमाभावयुक्तलुङ्', 'आशीर्लिङ्', ]
	lakarashort = ['law', 'laN', 'viliN', 'low', 'lfw', 'lfN', 'luw', 'liw', 'luN', 'aluN', 'AliN']
	searchedlakara = lakaralist[lakarashort.index(lakara)]
	url = "http://sanskrit.inria.fr/cgi-bin/SKT/sktconjug?lex=MW&q=" + verb +"&t=SL&c=" + gana + "&font=deva"
	response = urllib2.urlopen(url)
	#print "webpage downloaded at ",
	#timestamp()
	html_doc = response.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	#print "soup made at ",
	#timestamp()
	interestingdiv = soup.find("div", { "class" : "center" })
	tables = interestingdiv.findAll("table", { "class" : "mauve_cent" })
	for table in tables:
		interestingheader = unicode(table.tr.th.span.string)
		if interestingheader == searchedlakara.decode('utf-8'):
			return table
			break

def selecttable(text):
	input = text.split('.')
	verb = input[0]
	gana = input[1]
	pada = input[2]
	lakara = input[3]
	vacya = input[4]
	purusa = input[5]
	vacana = input[6]
	if input[4] == 'm':
		abbr = input[4]
	else:
		abbr = input[2]
	fulllist = ['परस्मैपदे', 'आत्मनेपदे', 'कर्मणि', ]
	abbrlist = ['p', 'A', 'm']
	searchedtype = fulllist[abbrlist.index(abbr)]
	searchedtype = searchedtype.decode('utf-8')
	inputtable = selectlakara(text)
	tables = inputtable.findAll("table", { "class" : "inflexion" })
	for table in tables:
		interestingtable = unicode(table.tr.th.span.string)
		if interestingtable == searchedtype:
			return table
			break

# function scrapeverbtable to scrape the data from verb in 3*3 format
def scrapverbtable(text):
	input = text.split('.')
	verb = input[0]
	gana = input[1]
	pada = input[2]
	lakara = input[3]
	vacya = input[4]
	purusa = input[5]
	vacana = input[6]
	tin = []
	selectedtable = selecttable(text)
	for row in selectedtable.findAll("tr"):
		cells = row.findAll("th")
		for cell in cells:
			tin.append(cell.text)
	return tin
		
# function 'v' for verb declention
""" The input format should be verb.gana.pada.lakara.vacya.purusa.vacana format. 
'gana' takes '1' to '10' where they are usual gaNas in pANini's grammar. Use '0' for secondary verbs.
'pada' takes 'p'/'a' for parasmaipada and Atmanepada respectively.
'lakara' takes 'law'/'laN'/'viliN'/'low'/'lfw'/'lfN'/'luw'/'liw'/'luN'/'aluN'/'AliN'. viliN stands for viDiliN. aluN stands for AgamAbhAvayuktaluN, AliN stands for ASIrliN. All others have their usual notations in pANini's grammar.
'vacya' takes 't' / 'm' for kartari and karmaNi respectively.
'purusa' takes 'p'/'m'/'u' for prathama, madhyama, uttama respectively.
'vacana' takes '1'/'2'/'3' for ekavacana, dvivacana and bahuvacana respectively.
"""

def v(text):
	input = text.split('.')
	verb = input[0]
	gana = input[1]
	pada = input[2]
	lakara = input[3]
	vacya = input[4]
	purusa = input[5]
	vacana = input[6]
	tinnumber = input[5] + "." + input[6]
	tin = scrapverbtable(text)
	tinlist = ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3']
	numlist = [5,6,7,9,10,11,13,14,15]
	return tin[numlist[tinlist.index(tinnumber)]]

# function 'd' for declention. It decides the proper declention function to chose i.e. 's' or 'v'
def d(text):
	input = text.split('.')
	if input[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
		return v(text).strip()
	elif input[1] in ['m', 'f', 'n', 'a']:
		return s(text).strip()
	else:
		print "Error in format of word entered."
		return "????"

# function dictconverter to parse document written in SanskritMark and render output.
# This function converts a file of SanskritMark words into Devanagari output file. The input file must have only one word in each line.
def dictconverter(inputfile,outputfile):
	with open(inputfile) as f:
		content = f.readlines()
	out = []
	for line in content:
		line = line.strip()
		out.append(d(line))
	with codecs.open(outputfile, "w", "utf-8-sig") as temp:
		for member in out:
			temp.write(member.strip() + "\n")
		temp.close()

# function parser to parse document written in SanskritMark and render output.
# The input should be stored in a file. words must be separated by space.
def parser(inputfile,outputfile):
	with open(inputfile) as f:
		content = f.readlines()
	out = []
	g = codecs.open(outputfile, 'w', 'utf-8-sig')
	for line in content:
		line = line.strip()
		words = re.split('([ ,?"!]+)', line)
		print words
		for x in xrange(len(words)):
			if x%2 == 0 and words[x].endswith('.'):
				g.write(d(words[x]) + ".")
			elif x%2 == 0 and not words[x].endswith('.'):
				g.write(d(words[x]))
			else:
				g.write(words[x])
		g.write("\n")
	g.close()

parser("input.txt", "output.txt")
