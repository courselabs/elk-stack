

## Play size - lines and characters

http://localhost:5601/app/visualize#/create?type=line&indexPattern=be237e90-d8cb-11eb-9476-01fc49d950bd&_g=(filters:!(),refreshInterval:(pause:!t,value:900000),time:(from:now-24h,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:be237e90-d8cb-11eb-9476-01fc49d950bd,key:type.keyword,negate:!f,params:(query:line),type:phrase),query:(match_phrase:(type.keyword:line)))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Lines),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Play,field:play_name,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:100),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Speaker,field:speaker),schema:metric,type:cardinality)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f),labels:(),legendPosition:right,seriesParams:!((data:(id:'1',label:Lines),drawLinesBetweenPoints:!t,interpolate:linear,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:line,valueAxis:ValueAxis-1),(data:(id:'3',label:Speaker),drawLinesBetweenPoints:!t,interpolate:linear,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-2)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:line,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Lines),type:value),(id:ValueAxis-2,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:RightAxis-1,position:right,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Speaker),type:value))),title:'',type:line))


docker-compose -f labs/kibana-query/compose-loader.yml up

- new index pattern

> reproduce parts of  https://www.elastic.co/blog/movember-data-dive-part-1



### Credits

Data adapted from https://github.com/elastic/examples/tree/master/Exploring%20Public%20Datasets/cdc_nutrition_exercise_patterns