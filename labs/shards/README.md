# Shards and Replicas

## Setup

On WSL2:

```
wsl -d docker-desktop sysctl -w vm.max_map_count=262144
```

Others:

```
sudo sysctl -w vm.max_map_count=262144
```

Run first Elasticsearch node:

```
docker-compose -f labs/shards/compose.yml up -d es01

docker logs elkstack_es01_1 -f
```

Shakespeare:

- settings use 6 shards w/ 2 replicas each

```
tar -xzf labs/aggregation/data/shakespeare.tar.gz

curl -H 'Content-Type: application/json' -XPUT 'http://localhost:9201/shakespeare' --data-binary "@labs/shards/mappings/shakespeare.json"

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9201/_bulk' --data-binary "@shakespeare_6.0.json"
```

Check the indices & document count:

```
curl http://localhost:9201/_cat/indices?v=true
```

> health=yellow

## CAT and admin APIs

- [compact and aligned text (CAT) APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat.html)

Cluster health:

```
curl http://localhost:9201/_cat/health?v=true
```

> unassign=3, active_shards_percent=50

Shards:

```
curl http://localhost:9201/_cat/shards?v=true
```

curl -H 'Content-Type: application/json' 'http://localhost:9201/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker-optimized.json"

## Add another node

docker-compose -f labs/shards/compose.yml up -d es02

docker logs elkstack_es02_1 -f

> `[es02]master node changed {previous [], current [{es01}`


curl http://localhost:9201/_cat/shards?v=true

Query es02 node:

curl -H 'Content-Type: application/json' 'http://localhost:9202/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker-optimized.json"

> all p=STARTED, one r=STARTED, one unassigned

## And another

docker-compose -f labs/shards/compose.yml up -d es03

docker logs elkstack_es03_1 -f

curl http://localhost:9203/_cat/shards?v=true

Try a query:

curl -H 'Content-Type: application/json' 'http://localhost:9201/shakespeare/_search?pretty=true&size=0' --data-binary "@labs/aggregation/lab/agg-text_entry-by-speaker-optimized.json"

## Lab

take es01 offline

docker-compose -f labs/shards/compose.yml stop es01

- is the cluster still healthy?

- what happened to the primary shards?

- does the query still work?

- add es04 - what happens to the cluster and shards?

- what happens to cluster and shards when es01 comes back online?