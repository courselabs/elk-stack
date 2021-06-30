# Running Logstash

## Run ELK

```
docker-compose -f labs/pipelines/compose.yml up -d

...logs -f
```

> logstash recreated, new volume mount

## Apache

- labs\pipelines\data-available/apache_small_logs
- labs\pipelines\pipelines\apache-to-es.conf
- labs\pipelines\pipeline-config\apache-to-es.yml

```
#TODO: -f or --force on linux; -force on windows
cp -force labs/pipelines/pipeline-config/apache-to-es.yml labs/pipelines/config/pipelines.yml
```

```
cp labs/pipelines/data-available/apache_small_logs labs/pipelines/data/apache_logs
```

Kibana

- create index pattern for 17 June logs
- verify field split

> apache-2021.06.17 - 20 hits

what is host field?

> docker exec elkstack_logstash_1 hostname

## Multiple indices

```
cp labs/pipelines/data-available/apache_logs labs/pipelines/data/apache_logs
```

Kibana

- index pattern for may 2021
- index pattern for all 2021


> apache-2021.05.* - 10019 
> apache-2021.* - 10040 docs

## Multiple pipelines

List plugins:

```
docker exec elkstack_logstash_1 bin/logstash-plugin list
```

- labs\pipelines\pipelines\http_poller-to-es.conf
- labs\pipelines\pipeline-config\all-to-es.yml

```
#TODO: -f or --force on linux; -force on windows
cp -force labs/pipelines/pipeline-config/all-to-es.yml labs/pipelines/config/pipelines.yml
```

- kibana

- index name doesn't allow searching across two hosts within one period

build visualization to show average response time as gauges:

![](/img/pipelines/http-response-times.png)

> http://localhost:5601/app/visualize#/create?type=gauge&indexPattern=1b8a5260-d990-11eb-9bc3-a33c8a14880b&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-1y,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(field:http_poller_metadata.runtime_seconds),schema:metric,type:avg),(enabled:!t,id:'2',params:(field:tags.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTooltip:!t,gauge:(alignment:automatic,backStyle:Full,colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:0.1),(from:0.1,to:0.75),(from:0.75,to:1.5)),extendRange:!t,gaugeColorMode:Labels,gaugeStyle:Full,gaugeType:Arc,invertColors:!f,labels:(color:black,show:!t),orientation:vertical,percentageMode:!f,scale:(color:'rgba(105,112,125,0.2)',labels:!f,show:!t),style:(bgColor:!t,bgFill:'rgba(105,112,125,0.2)',bgMask:!f,bgWidth:0.9,fontSize:60,mask:!f,maskBars:50,subText:'',width:0.9),type:meter),isDisplayWarning:!f,type:gauge),title:'',type:gauge))

## lab

- add simple csv loader
- source: simple.csv
- translate codes to desc
- how many events are not OK?

### Credits

https://github.com/elastic/examples/tree/master/Common%20Data%20Formats/apache_logs