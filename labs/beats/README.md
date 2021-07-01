
## Setup

docker-compose -f labs\beats\compose.yml up -d

http://localhost:5601


## Filebeat to Elasticsearch indes

- labs\beats\config\simplecsv-to-es.yml
- labs\beats\filebeat-simplecsv.yml

docker-compose -f labs\beats\filebeat-simplecsv.yml up -d

docker logs elkstack_filebeat-simplecsv_1 -f

> `Loading and starting Inputs completed. Enabled inputs: 1`

cp data/simple-small-1.csv labs/beats/data/


## Filebeat modules

> Pipeline & dashboard

- docker\filebeat\apache.yml
- labs\beats\filebeat-apache.yml

docker-compose -f labs\beats\filebeat-apache.yml up -d


- Kibana console

GET _ingest/pipeline

GET _template


> Grok pattern for Apache - beats send raw data to ES; pipeline processes doc

cp data/apache_logs-small labs/beats/data

docker logs elkstack_filebeat_1 -f

ls labs/beats/data

> File still there, Filebeat keeps an open read

Kibana

- discover, filebeat index - timeline 1 yr
- standard formatting
- dashboard

## Beats to Elasticsearch via Logstash

- labs\beats\pipelines\filebeat-pipeline.conf

docker-compose -f labs\beats\filebeat-apache.yml -f labs\beats\filebeat-simplecsv.yml down

> Ignore errors

rm -fo labs/beats/data/

docker-compose -f labs\beats\logstash.yml up -d

docker-compose -f labs\beats\logstash.yml logs -f

> `Connection to backoff(async(tcp://logstash:5044)) established`

- kibana, list indices `filebeat-7.10.2-apache` and `fb-ls-simplecsv`


cp data/apache_logs-2021* labs/beats/data/


cp data/simple.csv labs/beats/data/

kibana

- new index patterns
- discover

## Lab

use the `filebeat-7.10.2-apache` index for the apache dashboard
