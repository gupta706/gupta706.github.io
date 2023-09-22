#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file converts BibTeX files into jemdoc markup. 

import sys
import os
import re
import time
import StringIO
from subprocess import *
import tempfile

class controlstruct(object):
	def __init__(self, infile, outfile=None, conf=None, inname=None):
		self.inname = inname
		self.inf = infile
		self.outf = outfile
		self.conf = conf
		self.linenum = 0
		self.otherfiles = []
		self.texlines = []
		self.analytics = None
		self.eqbd = {} # equation base depth.
		self.baseline = None

	def pushfile(self, newfile):
		self.otherfiles.insert(0, self.inf)
		self.inf = open(newfile, 'r')

	def nextfile(self):
		self.inf.close()
		self.inf = self.otherfiles.pop(0)

def out(f, s):
	f.write(s)
	f.flush()

def hb(f, tag, content1, content2=None):
	"""Writes out a halfblock (hb)."""
	if content1 is None:
		content1 = ""

	if content2 is None:
		out(f, re.sub(r'\|', content1, tag))
	else:
		r = re.sub(r'\|1', content1, tag)
		r = re.sub(r'\|2', content2, r)
		out(f, r)

def procfile(f):
	prevyear = "8723467868235"
	lastnote = "nothing"

	f.outf.write("# jemdoc: menu{MENU}{publications.html}")
	f.outf.write("\n")
	f.outf.write("# jemdoc: addcss{jemdoc_custom.css}")
	f.outf.write("\n")
	f.outf.write("= Publications")
	f.outf.write("\n")
	f.outf.write("\n")
	
	papers_dict = {}
	num = 0
	for l in f.inf:
		l = l.strip()
		while "#" in l:
			l = removeConcat(l)
		if l.startswith("@"):
			title = None
			author = None
			authorstring = None
			btitle = None
			pgs = None
			yr = None
			org = None
			doi = None
			vol = None
			fullname = None
			school = None
			num = None
			address = None
			month = None
			note = None
		elif l != "}":
			if "=" in l:
				l = lowercaseFirstWord(l)
			if l.startswith('title'):
				title = l.strip('title')
				title = extract(title)
			elif l.startswith("author"):
				author = l.strip('author')
				author = extract(author)
				if "and" in author:
					a = author.split(" and ")
					afname = []
					for i in range(len(a)):
						current = a[i]
						fullname = ""
						# Checks if author names are in format "last name, first name"
						if ", " in current: 
							current = current.split(", ")
							#removes any random spacing from author names
							for k in range(len(current)):
								current[k] = current[k].strip()
							if i < len(a)-1:
								fullname = current[len(current)-1]+" "+current[0]
							elif i is len(a) - 1:
								fullname = current[len(current)-1]+" "+current[0]
							afname.append(fullname)
							authorstring = afname[0]
						# If author names are in format "first name last name"
						else:
							fullname = current
							afname.append(fullname)
							authorstring = afname[0]
						if len(afname) > 1:
							if len(afname) == 2:
								authorstring = afname[0]+" and "+afname[1]
							else:
								i = 0
								for j in range(1, len(afname)-1):
									authorstring += ", " + afname[j]
									i = j
								authorstring += ", and " + afname[i+1]
				else: 
					if ", " in author:
						author = author.split(", ")
						for i in range(len(author)):
							author[i] = author[i].strip()
						fullname = author[len(author)-1]+" "+author[0]
						authorstring = fullname
					else: 
						authorstring = author.strip(" ")
				authorstring = emphasizeName(authorstring)
			elif l.startswith("booktitle") or l.startswith("journal"):
				if l.startswith("booktitle"):
					btitle = l.strip('booktitle')
				elif l.startswith("journal"):
					btitle = l.strip('journal')
				btitle = extract(btitle)
			elif l.startswith("pages"):
				pgs = l.strip('pages')
				pgs = extract(pgs)
			elif l.startswith("year"):
				yr = l.strip('year')
				yr = extract(yr)
			elif l.startswith("organization"):
				org = l.strip('organization')
				org = extract(org)
			elif l.startswith("doi"):
				doi = l.strip('doi')
				doi = extract(doi)
			elif l.startswith("volume"):
				vol = l.strip('volume')
				vol = extract(vol)
			elif l.startswith('school'):
				school = l.strip('school')
				school = extract(school)
			elif l.startswith('address'):
				address = l.strip('address')
				address = extract(address)
			elif l.startswith('number'):
				num = l.strip('number')
				num = extract(num)
			elif l.startswith('month'):
				month = l.strip('month')
				month = extract(month)
			elif l.startswith('note'):
				note = l.strip('note')
				note = extract(note)
				
		
		else:
			if yr != prevyear:
				prevyear = yr
				hb(f.outf,f.conf['yearheading'],yr)

			if doi is not None:
				hb(f.outf, f.conf['articletitlewithdoi'],doi+" "+title)
			elif doi is None:
				hb(f.outf, f.conf['articletitlenodoi'],title)

			if btitle is not None:
				if "submitted" in btitle or "preparation" in btitle:
					hb(f.outf, f.conf['authorsubmitted'],authorstring)
					hb(f.outf, f.conf['submitted'],btitle)
				else:
					hb(f.outf, f.conf['authors'],authorstring)
					hb(f.outf, f.conf['journaltitle'],btitle)
					#if vol is not None:
						#hb(f.outf, f.conf['volume'],vol)
						#if num is not None:
							#hb(f.outf, f.conf['number'],num)
					#if pgs is not None:
						#hb(f.outf, f.conf['pgs'],pgs)
			elif school is not None:
				hb(f.outf, f.conf['authorsubmitted'],authorstring)
				hb(f.outf, f.conf['school'],school)
				if address is not None:
					hb(f.outf, f.conf['address'],address)

			#if month is not None:
				#hb(f.outf, f.conf['month'],month)
			#hb(f.outf, f.conf['year'],yr)

			#prints space at the end of each entry
			f.outf.write("\n")

	#if f.outf is not sys.stdout:
		# jem: close file here.
		# jem: XXX this is where you would intervene to do a fast open/close.
		#f.outf.close()

def procthesis(f):
	hb(f.outf, f.conf['thesisheading'],"")
	for l in f.inf:
		l = l.strip()
		while "#" in l:
			l = removeConcat(l)
		if l.startswith("@"):
			title = None
			author = None
			authorstring = None
			btitle = None
			pgs = None
			yr = None
			org = None
			doi = None
			vol = None
			fullname = None
			school = None
			num = None
			address = None
			month = None
		elif l != "}":
			if "=" in l:
				l = lowercaseFirstWord(l)
			if l.startswith('title'):
				title = l.strip('title')
				title = extract(title)
			elif l.startswith("author"):
				author = l.strip('author')
				author = extract(author)
				if "and" in author:
					a = author.split(" and ")
					afname = []
					for i in range(len(a)):
						current = a[i]
						fullname = ""
						# Checks if author names are in format "last name, first name"
						if ", " in current: 
							current = current.split(", ")
							#removes any random spacing from author names
							for k in range(len(current)):
								current[k] = current[k].strip()
							if i < len(a)-1:
								fullname = current[len(current)-1]+" "+current[0]
							elif i is len(a) - 1:
								fullname = current[len(current)-1]+" "+current[0]
							afname.append(fullname)
							authorstring = afname[0]
						# If author names are in format "first name last name"
						else:
							fullname = current
							afname.append(fullname)
							authorstring = afname[0]
						if len(afname) > 1:
							if len(afname) == 2:
								authorstring = afname[0]+" and "+afname[1]
							else:
								i = 0
								for j in range(1, len(afname)-1):
									authorstring += ", " + afname[j]
									i = j
								authorstring += ", and " + afname[i+1]
				else: 
					if ", " in author:
						author = author.split(", ")
						for i in range(len(author)):
							author[i] = author[i].strip()
						fullname = author[len(author)-1]+" "+author[0]
						authorstring = fullname
					else: 
						authorstring = author.strip(" ")
				authorstring = emphasizeName(authorstring)
			elif l.startswith("booktitle") or l.startswith("journal"):
				if l.startswith("booktitle"):
					btitle = l.strip('booktitle')
				elif l.startswith("journal"):
					btitle = l.strip('journal')
				btitle = extract(btitle)
			elif l.startswith("pages"):
				pgs = l.strip('pages')
				pgs = extract(pgs)
			elif l.startswith("year"):
				yr = l.strip('year')
				yr = extract(yr)
			elif l.startswith("organization"):
				org = l.strip('organization')
				org = extract(org)
			elif l.startswith("doi"):
				doi = l.strip('doi')
				doi = extract(doi)
			elif l.startswith("volume"):
				vol = l.strip('volume')
				vol = extract(vol)
			elif l.startswith('school'):
				school = l.strip('school')
				school = extract(school)
			elif l.startswith('address'):
				address = l.strip('address')
				address = extract(address)
			elif l.startswith('number'):
				num = l.strip('number')
				num = extract(num)
			elif l.startswith('month'):
				month = l.strip('month')
				month = extract(month)
		else:

			if doi is not None:
				hb(f.outf, f.conf['articletitlewithdoi'],doi+" "+title)
			elif doi is None:
				hb(f.outf, f.conf['articletitlenodoi'],title)

			if btitle is not None:
				if "submitted" in btitle or "preparation" in btitle:
					hb(f.outf, f.conf['authorsubmitted'],authorstring)
					hb(f.outf, f.conf['submitted'],btitle)
				else:
					hb(f.outf, f.conf['authors'],authorstring)
					hb(f.outf, f.conf['journaltitle'],btitle)
					#if vol is not None:
						#hb(f.outf, f.conf['volume'],vol)
						#if num is not None:
							#hb(f.outf, f.conf['number'],num)
					#if pgs is not None:
						#hb(f.outf, f.conf['pgs'],pgs)
			elif school is not None:
				hb(f.outf, f.conf['authorsubmitted'],authorstring)
				hb(f.outf, f.conf['school'],school)
				if address is not None:
					hb(f.outf, f.conf['address'],address)

			#if month is not None:
				#hb(f.outf, f.conf['month'],month)
			#hb(f.outf, f.conf['year'],yr)

			#prints space at the end of each entry
			f.outf.write("\n")		

def emphasizeName(b):
	if "Abhishek Gupta" in b:
		b = b.replace("Abhishek Gupta","*Abhishek Gupta*")
	if "A. Gupta" in b:
		b = b.replace("A. Gupta","*Abhishek Gupta*")
	return b; 

def refine(b):
	print(b)
	while "{" in b and "}" in b:
		b = removebraces(b)
	while "\\" in b:
		b = replacelatex(b)
	return b

def extract(b):
	if '"' in b:
		b = b.strip(' =","')
	elif '{' in b:
		b = b.strip(' ={,}')
	b = refine(b)
	return b

def removebraces(b):
	#These remove any remaining curly braces that are used in LaTeX
	b = b[:b.index("{")] + b[b.index("{")+1:]
	b = b[:b.index("}")] + b[b.index("}")+1:]
	return b

def removeConcat(b):
	#Removes any concatenation from LaTeX formatting
	b1 = b.split("#")[:1]
	b1[0] = b1[0].strip()
	b1[0] = b1[0].strip("\"}{")
	b2 = b.split("#")[1:]
	b2[0] = b2[0].strip()
	b2[0] = b2[0].strip("\"}{")
	r = b1[0]+b2[0]
	return r

def lowercaseFirstWord(b):
	#Because BibTeX tags are not case sensitive and this program is, lowercases first word of entry
	f = b.split("=")[:1]
	f[0] = f[0].lower()
	r = b.split("=")[1:]
	l = f[0]+"="+r[0]
	return l

def replacelatex(b):
	#These are LaTeX special characters that should be replaced with their actual unicode counterparts.
	print(b)
	bsplit = b.split();
	print(b.split())
	bNew = ""
	for i in range(len(bsplit)):
		current = bsplit[i]
		if current.find("{\\") != -1:
			while "{" in current and "}" in current:
				current = removebraces(current)
		bNew = bNew + " "+ current

	bNew = bNew.replace("\\&", "&")
	bNew = bNew.replace("\\cs","ş")
	
	bNew = bNew.replace("\\\'a","á")
	bNew = bNew.replace("\\'e","é")
	bNew = bNew.replace("\\'i","í")
	bNew = bNew.replace("\\\'o","ó")
	bNew = bNew.replace("\\\'u","ú")
	bNew = bNew.replace("\\\'y","ý")
	bNew = bNew.replace("\\\'w","ẃ")

	bNew = bNew.replace("\\`o","ò")
	bNew = bNew.replace("\\`a","à")
	bNew = bNew.replace("\\`e","è")
	bNew = bNew.replace("\\`i","ì")
	bNew = bNew.replace("\\`u","ù")
	bNew = bNew.replace("\\`w","ẁ")
	bNew = bNew.replace("\\`y","ỳ")
	bNew = bNew.replace("\\^a","â")
	bNew = bNew.replace("\\^e", "ê")
	bNew = bNew.replace("\\^i", "î")
	bNew = bNew.replace("\\^o", "ô")
	bNew = bNew.replace("\\^u", "û")
	bNew = bNew.replace("\\^w", "ŵ")
	bNew = bNew.replace("\\^y", "ŷ")
	
	bNew = bNew.replace("\\\"a", "ä")
	bNew = bNew.replace("\\\"e", "ë")
	bNew = bNew.replace("\\\"i", "ï")
	bNew = bNew.replace("\\\"o", "ö")
	bNew = bNew.replace("\\\"u", "ü")
	bNew = bNew.replace("\\\"w", "ẅ")
	bNew = bNew.replace("\\\"y", "ÿ")

	return bNew

def standardconf():
	a = """

	[thesisheading]
== Thesis

	[yearheading]
== |

	[articletitlewithdoi]
: {*[|]*}

	[articletitlenodoi]
: {*|*}

	[authors]
 |\\n

 	[authorsubmitted]
 |\\n

 	[submitted]
 |\\n

	[journaltitle]
 /|/\\n

 	[org]
 |\\n

	[school]
 |\\n

	[address]
 |\\n 

	[volume]
vol. |, 

	[number]
no. |,

	[pgs]
pp. |, 

	[month]
|, 

	[year]
|.

	"""
	b = ''
	for l in a.splitlines(True):
		if l.startswith('  '):
			b += l[2:]
		else:
			b += l

	return b

def pc(f, ditchcomments=True):
	"""Peeks at next character in the file."""
	# Should only be used to look at the first character of a new line.
	c = f.inf.read(1)
	if c: # only undo forward movement if we're not at the end.
		if ditchcomments and c == '#':
			l = nl(f)
			if doincludes(f, l):
				return "#"

		if c in ' \t':
			return pc(f)

		if c == '\\':
			c += pc(f)

		f.inf.seek(0, 1)
	elif f.otherfiles:
		f.nextfile()
		return pc(f, ditchcomments)

	return c

def readnoncomment(f):
	l = f.readline()
	if l == '':
		return l
	elif l[0] == '#': # jem: be a little more generous with the comments we accept?
		return readnoncomment(f)
	else:
		return l.rstrip() + '\n' # leave just one \n and no spaces etc.

def parseconf(cns):
	syntax = {}
	warn = False # jem. make configurable?
	# manually add the defaults as a file handle.
	fs = [StringIO.StringIO(standardconf())]
	for sname in cns:
		fs.append(open(sname, 'rb'))
	for f in fs:
		while pc(controlstruct(f)) != '':
			l = readnoncomment(f)
			r = re.match(r'\[(.*)\]\n', l)
			if r:
				tag = r.group(1)
				s = ''
				l = readnoncomment(f)
				while l not in ('\n', ''):
					s += l
					l = readnoncomment(f)
				syntax[tag] = s
		f.close()
	return syntax

def main():
	outoverride = False
	confoverride = False
	outname = None
	confnames = []
	for i in range(1, len(sys.argv), 2):
		if sys.argv[i] == '-o':
			if outoverride:
				raise RuntimeError("only one output file / directory, please")
			outname = sys.argv[i+1]
			outoverride = True
		elif sys.argv[i] == '-c':
			if confoverride:
				raise RuntimeError("only one config file, please")
			confnames.append(sys.argv[i+1])
			confoverride = True
		elif sys.argv[i].startswith('-'):
			raise RuntimeError('unrecognised argument %s, try --help' %sys.argv[i])
		else:
			break

	conf = parseconf(confnames)

	inname = None
	for j in range(0, len(sys.argv)):
		# First, if not a file and no dot, try opening .jemdoc. Otherwise, fall back
		# to just doing exactly as asked.
		inname = sys.argv[j]
		if not os.path.isfile(inname) and '.' not in inname:
			inname += '.bib'

	if outname is None:
		thisout = re.sub(r'.bib$', '', inname) + '.jemdoc'
	elif os.path.isdir(outname):
		# if directory, prepend directory to automatically generated name.
		thisout = outname + re.sub(r'.bib$', '', inname) + '.jemdoc'
	else:
		thisout = outname

	infile = open(inname, 'r')
	outfile = open(thisout, 'w')

	f = controlstruct(infile, outfile, conf, inname)
	procfile(f)

	if os.path.isfile("thesis.bib"):
		thesisfile = open("thesis.bib",'r')
		f2 = controlstruct(thesisfile, outfile, conf, inname)
		procthesis(f2)

	infile.close();
	outfile.close();
	if f.outf is not sys.stdout:
		# jem: close file here.
		# jem: XXX this is where you would intervene to do a fast open/close.
		f.outf.close()	

if __name__ == '__main__':
	main()
