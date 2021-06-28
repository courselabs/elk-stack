# Lab Solution


curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/students/_bulk' --data-binary "@labs/for-search/lab/data/students.json"



- bulk load students
- how many "Chiefs"?
- who is the CTO of Globomantics?

curl -H 'Content-Type: application/json' http://localhost:9200/students/_search?pretty=true --data-binary "@labs/for-search/lab/queries/match-role-chief.json"

> 2

curl -H 'Content-Type: application/json' http://localhost:9200/students/_search?pretty=true --data-binary "@labs/for-search/lab/queries/match-role-cto.json"

> Vilma Macdonald

