
Pipeline & conf:

- labs\pipelines\lab\simplecsv-to-es.conf
- labs\pipelines\lab\all-to-es.yml

Copy pipeline first:

```
cp -force labs/pipelines/lab/simplecsv-to-es.conf labs/pipelines/pipelines/
```

Then config:

```
cp -force labs/pipelines/lab/all-to-es.yml labs/pipelines/config/pipelines.yml
```

Check logs for OK:

```
Pipelines running {:count=>3, :running_pipelines=>[:"apache-to-es", :"http_poller-to-es", :"simplecsv-to-es"], :non_running_pipelines=>[]}
```

Copy data:

cp labs/pipelines/data-available/simple.csv labs/pipelines/data/

Kibana:

- index pattern = simplecsv
- filter NOT event_description.keyword: OK

> 40