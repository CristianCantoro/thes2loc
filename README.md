thes2loc
========

Italian Thesaurus to Library of Congress Headings

USAGE:
`make get`
Retrieve data from Wikidata (list of items with property BNCF Thesaurus) and from Wikimap (LCHS -> enwiki article titles)
`make resolve`
Retrieve data from Wikidata (BNCF Thesaurus item id, itwiki article title, enwiki aticle title)
`python thes2lsch.py`
Build thes2lsch.map with (BNCF Thesaurus item id, relation type, LCHS id, Wikidata item no.)

To retrieve the corresponding URLs:
* BNCF Thesaurus: http://thes.bncf.firenze.sbn.it/termine.php?id={thes_id}
* LCSH: http://id.loc.gov/authorities/subjects/{lhcs_id}.html
* Wikidata: http://www.wikidata.org/wiki/Q{wikidata_id}

Based on (this Gist)[https://gist.github.com/atomotic/7229203] by @atomotic.
