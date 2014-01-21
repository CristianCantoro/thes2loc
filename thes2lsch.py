#! /usr/bin/env python

import csv
import requests
import urlparse

FIELDNAMES_WIKIMAP = ('LC_head', 'relation', 'enwiki')
FIELDNAMES_RESOLVMAP = ('wikidata', 'thes_id', 'itwiki', 'enwiki')
FIELDNAMES_THES2LSCH = ('thes_id', 'relation', 'lc_head_id', 'wikidata')

LOCH_BASEURL = 'http://id.loc.gov/authorities/label/'

with open('wikimap.txt', 'r') as f:
    with open('resolv.map', 'r') as f2:

        wikimap = csv.DictReader(
            filter(lambda row: row[0]!='#', f),
            FIELDNAMES_WIKIMAP,
            delimiter='|'
            )

        resolvmap = csv.DictReader(
            filter(lambda row: row[0]!='#', f2),
            FIELDNAMES_RESOLVMAP,
            quotechar='"',
            delimiter=',',
            dialect=csv.QUOTE_ALL
            )

        enwiki_titles = {
            r['enwiki'].strip().strip('"'): r
            for r in resolvmap
            }

        for line in wikimap:
            with open('thes2lsch.map', 'a+') as f3:
                writer = csv.DictWriter(f3, FIELDNAMES_THES2LSCH)
                if line['enwiki'] in enwiki_titles:
                    resolv = enwiki_titles[line['enwiki']]
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

                        # import pdb
                        # pdb.set_trace()

                        writer.writerow(diz)

                