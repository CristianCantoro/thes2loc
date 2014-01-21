#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autore: Cristian Consonni <kikkocristian@gmail.com>
# Inspired by this gist by atomotic: 
# https://gist.github.com/atomotic/7229203
#
# The code is released with an MIT license
# please see the LICENSE file for details.

import sys
import csv

# My pywikibot installation is not working as it should be.
# So I have downloaded the code from:
# http://tools.wmflabs.org/pywikibot/
# and extracted it in the current directory
# Now I have a "core" directory in the current dir.
sys.path.append('core')

import pywikibot

q = "Q{}".format(sys.argv[1])
 
site = pywikibot.Site('it','wikipedia')
repo = site.data_repository()
item = pywikibot.ItemPage(repo, q)

try:
    data = item.get()
except pywikibot.exceptions.NoPage as e:
    print  "Error fetching item Q{}".format(sys.argv[1])
    exit(0)

thes = item.claims['P508'][0].getTarget()
 
itwiki = u''
try:
    itwiki = data['sitelinks']['itwiki']
except KeyError:
    pass

enwiki = u''
try:
    enwiki = data['sitelinks']['enwiki']
except KeyError:
    pass

OUTFILENAME = 'resolv.map'
FIELDNAMES = ('wikidata_id', 'thes_id', 'itwiki', 'enwiki')

out =  open(OUTFILENAME, "a+")

writer = csv.DictWriter(out, FIELDNAMES)
elements = [sys.argv[1],
            thes.encode('utf-8'),
            itwiki.encode('utf-8'),
            enwiki.encode('utf-8'),
            ]

row = dict(zip(FIELDNAMES, elements))

try:
    writer.writerow(row)
except Exception as e:
    print "Error with row: ", e, row

out.close()
exit(0)
