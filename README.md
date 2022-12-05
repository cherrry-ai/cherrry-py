# cherrry-py

## Cherrry Python SDK

<img width="644" alt="CleanShot 2022-11-30 at 21 40 41@2x" src="https://user-images.githubusercontent.com/42971022/204960579-371f96b7-1281-4c7a-b95a-81e4c3139020.png">

## Installation + API keys

### pip package

Install with pip

```python
pip install cherrry
```

### API Keys

From https://cherrry.com/dashboard/api to get your API Keys

#### Private Key

Private keys start with `ch_prv`

**keep it secret and never use it client-side**. It has service role privilages: it can read + write data.

#### Public Key

Public keys start with `ch_pub`

They're intended to be use client-side and have read-only privilages.

### Initalize

```python
from cherrry import CherrryClient
```

initialize the client

```python
client = CherrryClient("your_api_key")
```

## Concepts

### Table

A table is a collection of documents.

### Document

A document is respresented as a JSON object literal with three fields: `text`, `image`, and `metadata`.
These fields are also JSON object literals, where the keys can be strings with any contents, and their values are also strings.

`text` and `image` are semantically searchable each by their type respectively. Each document must have either a `text` or `image` field. It can also have both fields.
`metadata` is used to store additional information and for filtering (feature in progress), it is an optional field.

## Basic Functions

### Create Table

```python
[success, error] = client.create_table("table_name")
```

### Insert a Doc

Documents must be of the following form

```python
{
    "text": {
        "a name for your text": "your desired text in a string"
    },
    "image": {
        "a name for your image": "a url to your downloadable image"
    },
    "metadata": {
        "key": "value"
    }
}
```

for example:

```python
[data, error] = client.table("recipes").insert({
    "text": {
        "name": "Octopus Cherry Pie"
    },
    "image": {
        "preview": "https://i.imgur.com/lFC8p0L.jpeg"
    },
    "metadata": {
        "author_name": "Davy Jones",
        "author_email": "octo@pus.com"
    }
})
```

### Search

```python
[data, error] = client
    .table("blogs")
    .search({ "prompt": "sea creature desert", "size": 1, "search_type": "image" });
```

### Get Doc by ID

The ID of documents are returned in the responses of `/search` or `/doc`

```python
[data, error] = client.table("blogs").doc("1234")
```

### Delete a Doc

```python
[success, error] = client.table("blogs").delete("1234")
```
