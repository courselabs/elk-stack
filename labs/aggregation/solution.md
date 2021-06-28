

Check basic query:

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?q=text_entry:coward'

Add to aggregation:

curl -H 'Content-Type: application/json' http://localhost:9200/shakespeare/_search?pretty=true --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker.json"

> Falstaff, 7 times :)

Efficiency - get list of types:

curl -H 'Content-Type: application/json' http://localhost:9200/shakespeare/_search?pretty=true --data-binary "@labs/aggregation/lab/agg-type.json"

> Line, scene and act

curl -H 'Content-Type: application/json' http://localhost:9200/shakespeare/_search?pretty=true --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker-optimized.json"