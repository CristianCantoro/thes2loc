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

It uses this mapping by John Ockerbloom:
[wikimap](https://github.com/JohnMarkOckerbloom/ftl/blob/master/data/wikimap)

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

* column in  `thes2lcsh.map` are 

`(thes_id, relation, lcsh_id, wikidata_id)`

where:
1) `thes_id` is the BNCF Thesaurus term identifier;
2) `relation` is the relation type 
(as defined by John Ockerbloom's classification, see the [documentation](https://github.com/JohnMarkOckerbloom/ftl/blob/master/data/docs);
3) `lcsh_id` is the Library of Congress Subject Heading identifier;
4) `wikidata_id` is the Wikidata item no. (e. g. `42` for `Q42`);

To retrieve the corresponding URLs from `thes2lcsh.map` use the following
mapping:
* for BNCF Thesaurus: `http://thes.bncf.firenze.sbn.it/termine.php?id={thes_id}`
* for LCSH: `http://id.loc.gov/authorities/subjects/{lhcs_id}.html`
* for Wikidata: `http://www.wikidata.org/wiki/Q{wikidata_id}`

Inspired by [this Gist](https://gist.github.com/atomotic/7229203)
by @atomotic.

License
-------

This software is released under the MIT license. It is free software.
(c) 2014 by Cristian Consonni