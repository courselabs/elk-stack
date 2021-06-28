# You Know, for Search

## REference

- [Index API]
- [Search API]
- [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)


## Installing Elasticsearch

The standard Elasticsearch install comes with its own Java installation and an additional set of paid features which need a trial license.

You don't want that for the cleanest installation. Find the latest release which:

- is fully open source software (OSS)
- comes without a Java runtime so you can install your own

And work out which versions of Java you can use to run Elasticsearch.

## Running Elasticsearch in a Docker container

- [Dockerfile]

- starts from a Docker image which has OpenJDK 11 installed
- downloads and expands the Elasticsearch 7.10 archive
- sets up the environment with a Linux user and Java options
- copies in the downloaded Elasticsearch directory & config files
- tells Docker to run the `/bin/elasticsearch` binary on startup

```
docker-compose -f labs/for-search/compose.yml up -d
```

```
docker logs elkstack_elasticsearch_1 
```

```
curl http://localhost:9200
```

What version are we running?

## Indexing documents

Indexing is how you store data in Elasticsearch. There are client libraries for all the major languages, and you can use the REST API.

_On Windows 10:_

```
. ./labs/scripts/windows-tools.ps1
```

```
curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/classes/_doc/elk-stack' --data-binary "@labs/for-search/data/elk-stack.json"
```

```
curl http://localhost:9200/classes/_doc/elk-stack
```

Add two more classes:

- id: docker-fun, file path: labs/for-search/classes/docker-fun.json
- id: k8s-fun, file path: labs/for-search/classes/k8s-fun.json

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/classes/_doc/docker-fun' --data-binary "@labs/for-search/data/docker-fun.json"

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/classes/_doc/k8s-fun' --data-binary "@labs/for-search/data/k8s-fun.json"

Check the details are stored:

```
curl http://localhost:9200/classes/_doc/docker-fun

curl http://localhost:9200/classes/_doc/k8s-fun
```



## Searching and filtering

Querystring:

curl http://localhost:9200/classes/_search?q=fundamentals

curl http://localhost:9200/classes/_search?q=-fundamentals

curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/for-search/queries/match-all.json"


curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/for-search/queries/match-name.json"

curl -H 'Content-Type: application/json' http://localhost:9200/classes/_search?pretty=true --data-binary "@labs/for-search/queries/match-bool-name.json"


> Mapping





## Lab

- load students
- update class