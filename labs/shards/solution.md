
curl http://localhost:9203/_cat/nodes?v=true

> No es01; either es02 or es03 is master

curl http://localhost:9203/_cat/shards?v=true

> Primaries on other nodes - promoted - and replicas unassigned

curl -H 'Content-Type: application/json' 'http://localhost:9203/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker-optimized.json"

docker-compose -f labs/shards/compose.yml up -d es04

curl http://localhost:9202/_cat/nodes?v=true

curl http://localhost:9202/_cat/shards?v=true

docker-compose -f labs/shards/compose.yml start es01

curl http://localhost:9202/_cat/shards?v=true

> P and r spread all around