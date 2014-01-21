.PHONY : get resolve match clean all

NCORES = 8

get:
	curl -s "http://208.80.153.172/api?q=claim\[508\]" | jq ".items[]" > ids.txt
	curl -s "https://raw.github.com/JohnMarkOckerbloom/ftl/master/data/wikimap"  > wikimap.txt 

resolve:
	parallel -j$(NCORES) ./make_resolver_map.py {} :::: ids.txt

match:
	./produce_enwiki_titles.py
	parallel -j$(NCORES) ./thes2lcsh.py {} :::: wikimap.txt 
	
all: | get resolve match

clean:
	rm ids.txt wikimap.txt
	rm resolv.map.pkl
	rm resolv.map thes2lsch.map
