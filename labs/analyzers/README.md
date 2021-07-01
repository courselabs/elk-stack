
- [Built-in analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/analysis-analyzers.html)
- [Custom analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/analysis-custom-analyzer.html)

## Setup

docker-compose -f labs\analyzers\compose.yml up -d

## Built-in analyzers

http://localhost:5601

dev tools:

```
GET _analyze
{
  "analyzer": "standard",
  "text": "Working with the ELK Stack"
}
```

> lowercase tokens

Use a different built-in analyzer to lowercase and remove common words ("stop words") - should return

- working
- elk
- stack

```
GET _analyze
{
  "analyzer": "stop",
  "text": "Working with the ELK Stack"
}
```

> Should use same analyzer at index time & query time

## Building custom analyzers


- 0..* character filters
- 1 tokenizer
- 0..* token filters
- 

An analyzer which does stemming

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "porter_stem" ],
  "text": "Working with the ELK Stack"
}

> add stop and lowercase to produce work,elk,stack

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "stop", "porter_stem", "lowercase" ],
  "text": "Working with the ELK Stack"
}


Add synonyms:

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "stop", "porter_stem", "lowercase", { "type": "synonym", "synonyms": [ "elk => elastic" ] ],
  "text": "Working with the ELK Stack"
}

What will the output be?

> work, elast, stack <- synonyms are stemmed too

## Creating indexes with custom analyzers

PUT /tech-classes
{
  "settings": {
    "analysis": {
      "analyzer": {
        "tech_analyzer": {
          "type": "custom", 
          "char_filter": [ "html_strip" ],
          "tokenizer": "standard",
          "filter": [ "stop", "lowercase", "tech_synonym", "porter_stem"  ]
        }
      },
      "filter": {
        "tech_synonym" : { 
          "type": "synonym", 
          "synonyms": [ "elk => elastic" ] 
          
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "tech_analyzer"
      }
    }
  }
}

POST /tech-classes/_analyze
{
  "analyzer": "tech_analyzer",
  "text": "Works with <b>Elastical Stack</b>"
}

POST /tech-classes/_analyze
{
  "analyzer": "tech_analyzer",
  "text": "Working with the ELK Stack"
}

> Order is important

## Searching with custom analyzers

POST /tech-classes/_doc/elk-stack
{ 
    "cid" : "elk-stack", 
    "name" : "Working with the ELK Stack",
    "description" : "Working with the ELK Stack",
    "labUrl" : "https://elkstack.courselabs.co"
}

GET /tech-classes/_search?q=elastic

> matches, default analyzer

GET /tech-classes/_search
{ 
    "query": 
    { 
        "match":  
        {
            "description":  "elastic"
        }
    } 
}

> no matches

GET /tech-classes/_search
{ 
    "query": 
    { 
        "match":  
        {
            "name":  "elastic"
        }
    } 
}

>  matches

