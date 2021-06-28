# Aggregation

## Reference

- 
## Setup

Run Elasticsearch:

```
docker-compose -f labs/aggregation/compose.yml up -d
```

Insert data:

```
tar -xzf labs/aggregation/data/shakespeare.tar.gz

curl -H 'Content-Type: application/json' -XPUT 'http://localhost:9200/shakespeare' --data-binary "@labs/aggregation/mappings/shakespeare.json"

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/_bulk' --data-binary "@shakespeare_6.0.json"
```

> takes longer, huge output

Check the indices & document count:

```
curl http://localhost:9200/_cat/indices?v=true
```

> shakespeare index with 111,396 docs

## Metrics aggregation

Cound of all plays

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/agg-value_count-play_name.json"

> No de-duplication

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/agg-cardinality-play_name.json"

> Distinct count

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/agg-cardinality-query-play_name.json"

> Queried count

## Bucket aggregation

```
curl http://localhost:9200/shakespeare/_mappings?pretty=true
```

> play & speaker are keyword only; text_entry is text + keyword

Find all the "Henry" plays:

curl -H 'Content-Type: application/json' http://localhost:9200/shakespeare/_search?pretty=true --data-binary "@labs/aggregation/queries/term-play_name.json"

> No matches, terms need to exactly match

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/wildcard-play_name.json"

> 10K+ matches => number of lines in Henry plays, not what we want

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/agg-play_name.json"

> All plays with line count

curl -H 'Content-Type: application/json' 'http://localhost:9200/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/queries/agg-filter-play_name.json"

> Henry plays with line count

## Lab

Who most often uses the insult "coward"?

There are different types of data  in the index; make the search efficient by only including 