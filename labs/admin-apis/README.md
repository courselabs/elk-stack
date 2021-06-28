# Admin APIs


## CAT and admin APIs

- [compact and aligned text (CAT) APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat.html)

Indices:

```
curl http://localhost:9200/_cat/indices?v=true
```

Get count of documents in ilt index:

```
curl http://localhost:9200/_cat/count/ilt?v=true
```


Cluster health:

```
curl http://localhost:9200/_cluster/health
```



## Lab
