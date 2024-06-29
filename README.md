# ox-doc

**ox_doc** is an open-source lib to handle documents read write of different data structures efficiently and serialization, deserialization and processing

## about :

when we need to store and retrive data we serialization it in file this approach involes loading entire data into memory and using the one we requir and update processes it and store it again but this involes too much computation and time

**ox_doc** is a lib to handel read write update delete of different data structures and serialise it with most efficiency by imploing different techniques for different data tructures and large data 


## Installation:

always build from source for latest and bug free version

### build from source :

```
pip install git+https://github.com/ox-ai/ox-doc.git
```
### from pip
```
pip install ox-doc
```
## docs :

- [docs.md](./docs/docs.md) will be released after major release


## ox_doc.ld :

+ **ld.OxDoc** : is a hybrid file fromat - virtual file(folder acts as file) with `.oxd` extention 

+ **ld.OxDoc** is used to store data as key-value pairs and is most efficient to use when the values are of large data and is needed to be fetched by key 

+ store key value data in a bson format, index the the key value positions efficiently to retrive it by pointing key - to position index

```py
key.type    = str
value.type  = any , [str,list,set,dict]
```
+ **ld.OxDoc**

+ to work with oxd file or to use it in your project refere [test.oxd](test.oxd.ipynb) and [docs.oxd](./docs/oxd.md) 

### code snippet :

```py
from ox_doc.ld import OxDoc 

doc = OxDoc('data')

doc.set("k1"," dummy data-1")
doc.get("k1")
doc.add({'key4': 'value4', 'key5': 'value5'})
doc.delete("k1")

doc.load_data()
```



## directory tree :

```tree
.
├── __init__.py
└── d1.py
```