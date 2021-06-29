
- [KQL](https://www.elastic.co/guide/en/kibana/7.10/kuery-query.html) - Kibana Query Language
## Setup

Run Elasticsearch & Kibana:

```
docker-compose -f labs/kibana-query/compose.yml up -d
```


Create an index called shakespeare with these mappings, using the Kibana Console:

```
{
    "mappings": {
      "properties": {
       "speaker": {"type": "keyword"},
       "play_name": {"type": "keyword"},
       "line_id": {"type": "integer"},
       "speech_number": {"type": "integer"}
      }
     }
    }
```

```
PUT /shakespeare
```

Load the data using Elasticsearch:


```
# unzip if you haven't:
tar -xzf labs/aggregation/data/shakespeare.tar.gz

# bulk load:
curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/_bulk' --data-binary "@shakespeare_6.0.json"
```

## Filter and search 

There's a speech in one of the plays full of intereting insults. Search for _three-suited_ to find out the speaker and the play.

> `"three-suited"`

You should get a single hit - filter on the play name and type of this document, to restrict further searches.

> Add to filter list: play_name: King Lear, type: line

Kibana is super easy to navigate. Using the search bar and field list you should be able to build a query which shows the speech containing that insult in full.

Searching is a lot about understanding the data structure:

- speaker stores the name of the character
- speech_number is the position of the speech within the scene
- line_number is the position of the line within the scene

Using those you can iterate over your query and narrow down. You're looking for this output from 11 matching documents:

![](/img/kibana-query/kents-insults.png)



> speaker: KENT and speech_number: 12 and  line_number: 2.2*

> select text_entry from the available fields to show just that value.

Who else uses the insult "rascal"? Which characters using that word have names starting with "H"?

> text_entry: "rascal" and not speaker: KENT

> text_entry: "rascal" and speaker: H*

## Exploring structured data

docker-compose -f labs/kibana-query/compose-loader.yml up

- add the new index pattern to kibana

 build a search which lists:

TV shows featuring David Attenborough, added to the catalog in 2016, with an "international" listing, sorted by the most recent releases.

"Africa"

> Filter, `type: TV Show`
Query: `cast: "David Attenborough" and date_added: "*2016" and listed_in: international`
Fields: release_year (desc)


what is the longest action/adventure movie about dragons?

"Di Renjie zhi Sidatianwang"

> Filter, `type:Movie`
Query: `listed_in: "Action & Adventure" and description: dragon`
Duration is a  text field - can't sort on it...

- img dragon-film 

## lab

- add scripted field duration_number

```
int duration = 0;
if (doc['type'].value == 'Movie') {
    String d = doc['duration.keyword'].value;
    if (d.endsWith(" min")) {
        duration = Integer.parseInt(d.substring(0, d.indexOf(" min")));
    }
}
return duration;
```

- img longest-dragon-film 

### Credits

https://www.kaggle.com/shivamb/netflix-shows

- https://github.com/logpai/loghub Shilin He, Jieming Zhu, Pinjia He, Michael R. Lyu. Loghub: A Large Collection of System Log Datasets towards Automated Log Analytics. Arxiv, 2020.


