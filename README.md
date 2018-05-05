# datastorex - provide abstraction for data manipulation over multiple data stores

#### supported datastore types are [“mysql”, “postgres”, “mariadb”, “sqlserver”, “oracle”, “mongodb”, “sqlite”]
#### Operators (=, >, <, !=, >=, <=, between, in, not in)


#### to insert data in data store :
```
>>> from datastorex import insert ;
>>> kwargs = { "connection_info": { "type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234" }, "tablename": "yoooo", "data_columns": ["attr9", "attr10", "attr5", "attr2"], "values": ["blah", "blah", "blah", "blah"] }
>>> 
>>> try:
...     datastorex.insert(**kwargs)
... except Exception, err:
...     raise err
... 
```

#### to update data in data store :
```
>>> from datastorex import update ;
>>> kwargs = { "connection_info": { "type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234" }, "tablename": "ohhlala", "filter": [ { "operand": "service_time", "operator": "between", "value": [ "2015-12-01 00:00:00", "2015-12-31 23:59:59" ] }, { "operand": "category", "operator": "=", "value": "beauty" }, { "operand": "city", "operator": "in", "value": [ "Bangalore", "Mumbai" ] } ], "set_columns": [ "attr5", "attr10" ], "set_values": [ 123, "blah blah" ] }
>>> 
>>> try:
...     datastorex.update(**kwargs)
... except Exception, err:
...     raise err
... 
```

#### to delete data in data store :
```

>>> from datastorex import delete ;
>>> kwargs = { "connection_info": { "type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234" }, "tablename": "ohhlala", "filter": [ { "operand": "service_time", "operator": "between", "value": [ "2015-12-01 00:00:00", "2015-12-31 23:59:59" ] }, { "operand": "category", "operator": "=", "value": "beauty" }, { "operand": "city", "operator": "in", "value": [ "Bangalore", "Mumbai" ] } ] }
>>> 
>>> try:
...     datastorex.delete(**kwargs)
... except Exception, err:
...     raise err
... 
```

#### to select data in data store :
```
>>> from datastorex import select ;
>>> kwargs = { "connection_info": { "type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234" }, "tablename": "ohhlala", "select_fields": [ "attr1", "attr2" ], "filter": [ { "operand": "service_time", "operator": "between", "value": [ "2015-12-01 00:00:00", "2015-12-31 23:59:59" ] }, { "operand": "category", "operator": "=", "value": "beauty" }, { "operand": "city", "operator": "in", "value": [ "Bangalore", "Mumbai" ] } ], "offset": "0", "limit": "20", "order_by": "attr1 desc" }
>>> 
>>> try:
...     datastorex.select(kwargs)
... except Exception, err:
...     print str(err)
... 
```


 
