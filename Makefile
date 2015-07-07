.PHONY : get resolve match clean all

NCORES = 8

get:
	curl -s "https://wdq.wmflabs.org/api?q=claim\[508\]" | jq ".items[]" > ids.txt
	curl -s "https://raw.githubusercontent.com/JohnMarkOckerbloom/ftl/master/data/wikimap"  > wikimap.txt 

resolve:
	parallel --no-notice -j$(NCORES) ./make_resolver_map.py {} :::: ids.txt

match:
	./produce_enwiki_titles.py
	parallel --no-notice -j$(NCORES) ./thes2lcsh.py {} :::: wikimap.txt 

distinct:
	cp thes2lcsh.map _thes2lcsh.map
	cat _thes2lcsh.map | sort | uniq > thes2lcsh.map
	rm _thes2lcsh.map

all: | get resolve match distinct

clean:
	rm ids.txt wikimap.txt
	rm resolv.map.pkl
	rm resolv.map thes2lsch.map
