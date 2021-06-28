# Lab Solution


Delete original and create alias:

curl -H 'Content-Type: application/json' -XDELETE 'http://localhost:9200/students' 

curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/_aliases' --data-binary "@labs/mappings/lab/alias.json"

Test alias:


curl -H 'Content-Type: application/json' http://localhost:9200/students/_search?pretty=true --data-binary "@labs/mappings/lab/queries/match-role.json"

> Should return sid-C1