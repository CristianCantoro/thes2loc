#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autore: Cristian Consonni <kikkocristian@gmail.com>
# Inspired by this gist by atomotic: 
# https://gist.github.com/atomotic/7229203
#
# The code is released with an MIT license
# please see the LICENSE file for details.

import csv
import pickle

INFILE = 'resolv.map'
PICKLE_FILE = 'resolv.map.pkl'

FIELDNAMES_RESOLVMAP = ('wikidata', 'thes_id', 'itwiki', 'enwiki')


if __name__ == '__main__':
    try:
        with open(INFILE, 'r') as infile:
            resolvmap = csv.DictReader(
                filter(lambda row: row[0]!='#', infile),
                FIELDNAMES_RESOLVMAP,
                quotechar='"',
                delimiter=',',
                dialect=csv.QUOTE_ALL
                )

            enwiki_titles = {
                r['enwiki'].strip().strip('"'): r
                for r in resolvmap
                }
    except IOError as e:
        print "Could not open file: {}".format(INFILE)
        print "make sure to call:"
        print "* make get"
        print "* make resolve"
        print "Before calling make match"
        exit(-1)

    with open(PICKLE_FILE, 'w') as outfile:
        pickle.dump(enwiki_titles, outfile)