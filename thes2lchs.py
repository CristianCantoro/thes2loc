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
import requests
import urlparse
import StringIO
import pickle

from produce_enwiki_titles import PICKLE_FILE

FIELDNAMES_WIKIMAP = ('LC_head', 'relation', 'enwiki')
FIELDNAMES_THES2LSCH = ('thes_id', 'relation', 'lc_head_id', 'wikidata')

LOCH_BASEURL = 'http://id.loc.gov/authorities/label/'

OUTFILE = 'thes2lcsh.map'

with open(PICKLE_FILE, 'r') as infile:
    enwiki_titles = pickle.load(infile)

f = StringIO.StringIO(sys.argv[1])

csvin = csv.DictReader(
    filter(lambda row: row[0]!='#', f),
    FIELDNAMES_WIKIMAP,
    delimiter='|'
    )

wikimap = [line for line in csvin]
if len(wikimap) == 1:
    line = wikimap[0]
    print "Process line: ", line
elif len(wikimap) == 0:
    print "Discard comments or empty lines", wikimap
    exit(0)
else:
    print "Error! Line too long: ", wikimap
    exit(-1)

finalout = open(OUTFILE, 'a+')

writer = csv.DictWriter(finalout, FIELDNAMES_THES2LSCH)

enwiki = line['enwiki']

if enwiki in enwiki_titles:
    resolv = enwiki_titles[enwiki]
    req = requests.get(LOCH_BASEURL+line['LC_head'])
    if req.ok:
        urlpath = urlparse.urlparse(req.url).path.split('/')[-1]
        lc_head_no = urlpath.replace('.html', '')

        fields = (resolv['thes_id'].strip().strip('"'),
                  line['relation'],
                  lc_head_no,
                  resolv['wikidata']
                  )

        diz =dict(zip(FIELDNAMES_THES2LSCH, fields))

        print "Writing: ", diz
        writer.writerow(diz)

    else:
        print "Error with request: ", line

finalout.close()
