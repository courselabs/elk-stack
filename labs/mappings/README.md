# Documents, Fields and Mappings

## Reference

- [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html)
- [term query](https://www.elastic.co/guide/en/elasticsearch/reference/current/term-level-queries.html)
- [explicit mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/explicit-mapping.html)

## Setup

Run Elasticsearch:

```
docker-compose -f labs/mappings/compose.yml up -d
```

Insert data:

```
curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/_bulk' --data-binary "@labs/mappings/data/classes-and-students.json"
```

Check the indices & document count:

```
curl http://localhost:9200/_cat/indices?v=true
```

> 2 indices, 3 & 9 docs

## Match and term searches




curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/mappings/queries/match-name.json"

curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/mappings/queries/term-name.json"

> 0

curl http://localhost:9200/classes/_mapping?pretty=true

curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/mappings/queries/term-name-keyword.json"

## Explicit mappings

curl http://localhost:9200/students/_mapping?pretty=true

> sid is long; inferred from data

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/students/_doc/elk-stack' --data-binary "@labs/mappings/data/student-C1.json"

> `failed to parse field [sid] of type [long]`

curl -H 'Content-Type: application/json' -XPUT 'http://localhost:9200/students/_mapping' --data-binary "@labs/mappings/mappings/students-sid.json"

> mapper [sid] cannot be changed from type [long] to [text]

New index with explicit mapping:

curl -H 'Content-Type: application/json' -XPUT 'http://localhost:9200/students2' --data-binary "@labs/mappings/mappings/students2.json"

curl http://localhost:9200/students2/_mapping?pretty=true

## Reindexing

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/_reindex' --data-binary "@labs/mappings/reindex-students.json"

curl http://localhost:9200/students2/_mapping?pretty=true

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/students2/_doc/elk-stack' --data-binary "@labs/mappings/data/student-C1.json"

curl -H 'Content-Type: application/json' http://localhost:9200/students2/_search?pretty=true --data-binary "@labs/mappings/queries/match-sid.json"

curl -H 'Content-Type: application/json' http://localhost:9200/students2/_search?pretty=true --data-binary "@labs/mappings/queries/wildcard-sid.json"


## Lab

- rename index

