thes2loc
========

Italian Thesaurus to Library of Congress Subject Headings via Wikidata

Why
---

`thes2loc` helps librarian building a multilingual 
[Thesarus](http://en.wikipedia.org/wiki/Thesaurus) in particular it finds
a mapping between the Italian 
[Tesauro del Nuovo Soggettario](http://thes.bncf.firenze.sbn.it)
from the Biblioteca Nazionale di Firenze (_National Library of Florence_)
and the Library of Congress Subject Headings.


Usage
------
USAGE:

`make all`

produces (among others) the file `thes2lcsh.map` which is what you are
interested in.

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
* for BNCF Thesaurus: 
  `http://thes.bncf.firenze.sbn.it/termine.php?id={thes_id}`
* for LCSH: `http://id.loc.gov/authorities/subjects/{lhcs_id}.html`
* for Wikidata: `http://www.wikidata.org/wiki/Q{wikidata_id}`

Inspired by [this Gist](https://gist.github.com/atomotic/7229203)
by @atomotic.

License
-------

This software is released under the MIT license. It is free software.
(c) 2014 by Cristian Consonni