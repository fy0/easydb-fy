# EasyDB [fy fork]

Warning:Incompatible with orgin project.

## EasyDB

A really simple **SQLite wrapper**.

It can be used on existing SQLite database:

```python
from easydb import EasyDB
db = EasyDB('filename.db')
cursor = db.query("SELECT * FROM mytable")
```

New databases can be creating by specifying your schema as a dictionary, eg:

```python
schema = {
    'table_name': ['column_name column_type', ...],
    'table_name': ['column_name column_type', ...],
}
db = EasyDB('filename.db', schema)
```

**If the database file already exists then the schema won't be updated, but if it doesn't exist then it'll be created with the given schema.**

A example:

```python
from easydb import EasyDB
db = EasyDB('my.db', {'users': ['name text', 'pw text']})

db.query("insert into users values('%s','%s')" % ('ben','123'))
# or: db.query("INSERT INTO users (name, pw) VALUES (?, ?)", ('ben', '123'))

print db.query("SELECT * FROM users")

# => (u'ben', u'123')
```

## kvDB

**Warning:Poor English**

A simple Key-Value style sqlite wrapper.

Here is a example:

```python
from easydb import EasyDB
db = kvDB('test.db')

db['test'] = '123456'

print db['test']

# => 123456
```

Something more interesting:

```python
from easydb import EasyDB
db = kvDB('test.db')

db['test'] = '123','456'

print db['test']

# => ('123', '456')
```

