import json
import os
from typing import Dict

import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch

index_name='netflix-2019'
mapping = {
    "mappings": {
        "properties": {
            "show_id": {"type": "text"},
            "type": {"type": "keyword"},
            "title": {"type": "text"},
            "director": {"type": "text"},
            "cast": {"type": "text"},
            "country": {"type": "keyword"},
            "date_added": {"type": "text"},
            "release_year": {"type": "short"},
            "rating": {"type": "keyword"},
            "duration": {"type": "text", "fields": {"keyword": { "type": "keyword" }}},
            "listed_in": {"type": "text"},
            "description": {"type": "text"},
        }
    }
}

# connect & create the index with explicit mapping:
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
es.indices.create(index=index_name, ignore=400, body=mapping)
print(f'Created index: {index_name}')

# read the CSV file:
df = pd.read_csv('./netflix_titles.csv').replace({np.nan: None})
print(f'Read CSV, rows: {len(df.index)}')

# insert a document for each row:
for doc in df.apply(lambda x: x.to_dict(), axis=1):
    es.index(index=index_name, body=json.dumps(doc))
    
print('Indexed all documents')