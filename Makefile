get:
	curl -s "http://208.80.153.172/api?q=claim\[508\]" | jq ".items[]" > ids.txt
	curl -s "https://raw.github.com/JohnMarkOckerbloom/ftl/master/data/wikimap"  > wikimap.txt 
resolve:
	parallel -j4 ./make_resolver_map.py {} :::: ids.txt > resolv.map
