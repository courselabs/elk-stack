

## Mapping

curl http://localhost:9200/classes/_mapping



curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/for-search/queries/match-name.json"

curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/for-search/queries/term-name.json"