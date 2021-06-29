

## Run Elasticsearch and Kibana

```
docker-compose -f labs/kibana/compose.yml up -d

docker logs elkstack_kibana_1 -f
```

> "http server running at http://0.0.0.0:5601"

curl http://localhost:9200/_cat/indices?v=true

> New ES, Kibana creates an index to store data

Browse to http://localhost:5601

## Use the Kibana Console

> http://localhost:5601/app/dev_tools#/console

```
GET /cat/indices
```

```
POST /classes/_doc/elk_stack
{ 
    "cid" : "elk-stack", 
    "name" : "Working with the ELK Stack",
    "labUrl" : "https://elkstack.courselabs.co"
}
```

```
POST /classes/_doc/docker-fun
{ 
    "cid" : "docker-fun", 
    "name" : "Docker Fundamentals",
    "labUrl" : "https://k8sfun.courselabs.co"
}
```

```
POST /classes/_doc/k8s-fun
{ 
    "cid" : "k8s-fun", 
    "name" : "Kubernetes Fundamentals",
    "labUrl" : "https://k8sfun.courselabs.co"
}
```

Autocomplete

- GET 
- /cl
- /_se
- {}
- que
- mat

```
GET /classes/_search
{
  "query": {
    "match": {
      "FIELD": "TEXT"
    }
  }
}
```


## Lab

View the data through Kibana, index pattern

