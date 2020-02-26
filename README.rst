pyphoton
========

🗺 Light Photon client written in Python

|Latest Version| |codecov| |Build Status| |License: MIT|

Install
-------

.. code:: sh

    pip install pyphoton

Usage
-----

Python Photon client allows you to make queries to Photon easily.

.. code:: py

    from pyphoton import Photon


    client = Photon()
    location = client.query('berlin', limit=1)

    print (location.city)
    print (location.latitude)
    print (location.longitude)

``Photon`` object accepts two parameters:

-  ``host``: the url where Photon instance is running (default
   ``https://photon.komoot.de``)
-  ``language``: the preferred language (default is ``en``)

You can pass to the ``query`` method the following parameters along the
query string:

-  ``limit``: limit number of results
-  ``language``: force language in the query
-  ``latitude`` and ``longitude``: use them to search with priority to a
   geo position
-  ``location_bias_scale``: use to search with location bias

``Location`` object (or objects if you don't set limit=1) is generated
from the json returned and contains all the information you need: name,
state, street, city, osm attributes, extent\_from.latitude,
extent\_from.longitude, extent\_to.latitude, extent\_to.longitude ...

If there's an with your query, a ``PhotonException`` will be raised

.. code:: py

    from pyphoton import Photon
    from pyphoton.errors import PhotonException


    client = Photon()
    try:
        location = client.query('', limit=1)
    except PhotonException as ex:
        print (ex)

WIP Features
------------

-  Reverse search
-  BBox search
-  Method to fetch latest data

Run tests
---------

.. code:: sh

    pip install -r requirements-dev.txt
    make test

.. |Latest Version| image:: https://img.shields.io/pypi/v/pyphoton.svg
   :target: https://pypi.python.org/pypi/pyphoton/
.. |codecov| image:: https://codecov.io/gh/astagi/pyphoton/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/astagi/pyphoton
.. |Build Status| image:: https://travis-ci.org/astagi/pyphoton.svg?branch=master
   :target: https://travis-ci.org/astagi/pyphoton
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/astagi/pyphoton/blob/master/LICENSE
