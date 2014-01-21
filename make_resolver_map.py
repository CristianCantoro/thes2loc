#!/usr/bin/env python
import sys
sys.path.append('core')

import pywikibot

q = "Q{}".format(sys.argv[1])
 
site = pywikibot.Site('it','wikipedia')
repo = site.data_repository()
item = pywikibot.ItemPage(repo, q)
 
data = item.get()

thes = item.claims['P508'][0].getTarget()
 
itwiki = None
try:
	itwiki = data['sitelinks']['itwiki']
	itwiki = itwiki.format('utf-8')
except KeyError:
	pass

enwiki = None
try:
	enwiki = data['sitelinks']['enwiki']
	enwiki = enwiki.format('utf-8')
except KeyError:
	pass

# import pdb
# pdb.set_trace()

print u'"{wikidata}", "{thes}", "{itwiki}", "{enwiki}"'.format(
	wikidata=sys.argv[1],
	thes=thes,
	itwiki=itwiki,
	enwiki=enwiki).encode('utf-8')
