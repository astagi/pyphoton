# pyphoton

🗺 Light Photon client written in Python

[![Latest Version](https://img.shields.io/pypi/v/pyphoton.svg)](https://pypi.python.org/pypi/pyphoton/)
[![codecov](https://codecov.io/gh/astagi/pyphoton/branch/master/graph/badge.svg)](https://codecov.io/gh/astagi/pyphoton)
[![Build Status](https://travis-ci.org/astagi/pyphoton.svg?branch=master)](https://travis-ci.org/astagi/pyphoton)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/astagi/pyphoton/blob/master/LICENSE)

## Install

```sh
pip install pyphoton
```

## Usage

If you need some code ready to use, [spike.py](https://github.com/astagi/pyphoton/blob/master/spike.py) is a good starting point

Python Photon client allows you to make queries to Photon service easily.

```py
from pyphoton import Photon


client = Photon()
location = client.query('berlin', limit=1)

print (location.city)
print (location.latitude)
print (location.longitude)
```

`Photon` object accepts two parameters:

- `host`: the url where Photon instance is running (default `https://photon.komoot.de`)
- `language`: the preferred language (default is `en`)

You can pass to the `query` method the following parameters along the query string:

- `limit`: limit number of results
- `language`: force language in the query
- `latitude` and `longitude`: use them to search with priority to a geo position
- `location_bias_scale`: use to search with location bias

`Location` object (or objects if you don't set limit=1) is generated from the json returned and contains all the information you need: name, state, street, city, osm attributes, extent_from.latitude, extent_from.longitude, extent_to.latitude, extent_to.longitude ...

If there's an error in your query, a `PhotonException` will be raised

```py
from pyphoton import Photon
from pyphoton.errors import PhotonException


client = Photon()
try:
    location = client.query('', limit=1)
except PhotonException as ex:
    print (ex)
```

## WIP Features

- Reverse search
- BBox search
- Query by osm tags
- Method to fetch latest data

## Run tests

```sh
pip install -r requirements-dev.txt
make test
```
