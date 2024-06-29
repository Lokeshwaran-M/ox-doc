# ox-doc

**ox_doc** is an open-source library designed to handle efficient reading, writing, serialization, deserialization, and processing of various data structures.

## About :

When storing and retrieving data, serialization into files is often required. This traditional approach involves loading the entire dataset into memory, processing the required portions, updating the data, and then storing it again. This process can be computationally expensive and time-consuming.

**ox_doc** addresses these inefficiencies by providing a library capable of handling read, write, update, and delete operations on different data structures. It optimizes serialization through various techniques tailored for different data structures, ensuring efficient processing of large datasets.

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

- **ld.OxDoc** : is a hybrid file fromat - virtual file(folder acts as file) with `.oxd` extention

- **ld.OxDoc** is used to store data as key-value pairs and is most efficient to use when the values are of large data and is needed to be fetched by key

- store key value data in a bson format, index the the key value positions efficiently to retrive it by pointing key - to position index

```py
key.type    = str
value.type  = any , [str,list,set,dict]
```

- **ld.OxDoc**

- to work with oxd file or to use it in your project refere [test.oxd](test.oxd.ipynb) and [docs.oxd](./docs/oxd.md)

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
