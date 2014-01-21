thes2loc
========

Italian Thesaurus to Library of Congress Headings

USAGE:

`make all`

This command comprises three other commands:

* `make get`: retrieves data from Wikidata (list of items with property BNCF
Thesaurus) and from Wikimap (LCHS -> enwiki article titles)

* `make resolve`: retrieves data from Wikidata (BNCF Thesaurus item id, itwiki
article title, enwiki aticle title)

* `make match`: builds thes2lsch.map with (BNCF Thesaurus item id, relation
type, LCHS id, Wikidata item no.)

To retrieve the corresponding URLs from the file `thes2lcsh.map` use the 
following mapping:

* column in  `thes2lcsh.map` are  `(thes_id, relation, lcsh_id, wikidata_id)`
* for BNCF Thesaurus: `http://thes.bncf.firenze.sbn.it/termine.php?id={thes_id}`
* for LCSH: `http://id.loc.gov/authorities/subjects/{lhcs_id}.html`
* for Wikidata: `http://www.wikidata.org/wiki/Q{wikidata_id}`

Inspired by [this Gist](https://gist.github.com/atomotic/7229203)
by @atomotic.
