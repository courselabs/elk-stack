# Running Logstash

## Run Logstash

```
docker-compose -f labs/logstash/logstash.yml up -d

docker logs elkstack_logstash_1 -f
```

- labs\logstash\pipelines\heartbeat.conf
- labs\logstash\pipeline-config\heartbeat.yml

> open a new terminal

```
#TODO: -f or --force on linux; -force on windows
cp -force labs/logstash/pipeline-config/heartbeat.yml labs/logstash/config/pipelines.yml
```

## CSV file input

- labs\logstash\data-available/simple-small-1.csv
- labs\logstash\pipelines\simplecsv.conf
- labs\logstash\pipeline-config\simplecsv.yml

```
#TODO: -f or --force on linux; -force on windows
cp -force labs/logstash/pipeline-config/simplecsv.yml labs/logstash/config/pipelines.yml
```

```
cp labs/logstash/data-available/simple-small-1.csv labs/logstash/data/
```

> Takes a moment to process, then output (async)


```
cp labs/logstash/data-available/simple-small-2.csv labs/logstash/data/
```

> Takes a moment to process, then output (async)

```
ls labs/logstash/data/
```

> files removed after processing

## The ELK Stack

Run Elasticsearch, Logstash &  Kibana:

```
docker-compose -f labs/logstash/compose.yml up -d
```

http://localhost:5601

- labs\logstash\pipelines\heartbeat-to-es.conf
- labs\logstash\pipeline-config\heartbeat-to-es.yml

```
#TODO: -f or --force on linux; -force on windows
cp -force labs/logstash/pipeline-config/heartbeat-to-es.yml labs/logstash/config/pipelines.yml
```

Kibana:

- add index pattern
- timestamp
- discover


## lab

simplcsv to es