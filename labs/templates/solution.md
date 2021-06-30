GET _cat/indices

POST _reindex
{
    "source": {
      "index": "apache2-2021.05.19"
    },
    "dest": {
      "index": "apache2-2021.05.19-2"
    }
}

DELETE /apache2-2021.05.19


 - etc.