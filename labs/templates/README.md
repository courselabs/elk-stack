
## Reference

- [Aliases](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/alias.html)

## Setup

```
docker-compose -f labs/templates/compose.yml up -d
```

> logstash recreated, new volume mount

Check running @ http://localhost:5601

Load May log file

```
cp labs/templates/data-available/apache_logs-2021-05 labs/templates/data/apache_logs
```

Kibana

- index pattern for may
- discover, can't filter response by range
- visualize, can't avg bytes

> apache2-2021.05.*

## Create index template

In Kibana console:

PUT _template/apache2
{
  "index_patterns": ["apache2*"],
  "settings": {
    "number_of_shards": 2, 
    "number_of_replicas" : 1,
    "query.default_field" : "request"
  },
  "mappings": {
    "properties": {
      "bytes": {
        "type": "integer"
      },
      "response": {
        "type": "short"
      },
      "httpversion": {
        "type": "float"
      },      
      "clientip": {
        "type": "ip"
      },      
      "referrer": {
        "type": "text"
      },      
      "agent": {
        "type": "text"
      }
    }
  }
}

GET /_cat/templates?v=true

GET /_template/apache2

GET /apache2-2021.05.25/_mapping

> All text+keyword; mappings for existing indices are not altered - only new indices


## Add more data

- labs\templates\pipelines\apache-to-es2.conf uses apache2 index prefix

```
cp labs/templates/data-available/apache_logs-2021-06 labs/templates/data/apache_logs
```

Kibana

- create index pattern for june 

> apache2-2021.06.*

- filter logs using http version above 1.0, with a response code between 401 and 403
- visualize bytes

- if logstash grok fails, writes a tag field; which log failed? how can you diagnose?

> filter tags exists; full message still stored - https://grokdebug.herokuapp.com, %{COMBINEDAPACHELOG} for pattern; missing double-quote at end :)

## Create alias

GET /_cat/aliases

PUT /apache2-2021.05.25/_alias/apache-logs-2021-05

Multiple indices in an alias:

PUT /apache2-2021.05.18/_alias/apache-logs-2021-05

GET _alias/apache-logs-2021-05

Aliases with index name pattern:

POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "apache2-2021.05.*",
        "alias": "apache-logs-2021-05"
      }
    }
  ]
}

> Can also include filter

GET /_cat/aliases/apache-logs-2021-05

Kibana

- index pattern for alias apache-logs-2021-05
- discover, click index field to see to pvalues
- visualize to see docs per index

## Add alias to index template

PUT _template/apache2
{
  "index_patterns": ["apache2*"],
  "aliases": {
    "apache2": {},
    "apache2-2021" : {}
  }
}

GET /_template/apache2

> Argh!

PUT _template/apache2
{
  "index_patterns": ["apache2*"],
  "settings": {
    "number_of_shards": 2, 
    "number_of_replicas" : 1,
    "query.default_field" : "request"
  },
  "aliases": {
    "apache2": {},
    "apache2-2021" : {}
  },
  "mappings": {
    "properties": {
      "bytes": {
        "type": "integer"
      },
      "response": {
        "type": "short"
      },
      "httpversion": {
        "type": "float"
      },      
      "clientip": {
        "type": "ip"
      },      
      "referrer": {
        "type": "text"
      },      
      "agent": {
        "type": "text"
      }
    }
  }
}


## lab 

reindex 05 indexes to new
make sure use new template