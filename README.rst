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

If you need some code ready to use,
`spike.py <https://github.com/astagi/pyphoton/blob/master/spike.py>`__
is a good starting point

Execute queries
~~~~~~~~~~~~~~~

Python Photon client allows you to make queries to Photon service
easily.

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

You can pass the ``query`` method the following parameters along the
query string:

-  ``limit``: limit number of results
-  ``language``: force language in the query
-  ``latitude`` and ``longitude``: use them to search with priority to a
   geo position
-  ``location_bias_scale``: use to search with location bias
-  ``osm_tags``: a ``string`` or ``list`` containing `osm tags
   filters <https://github.com/komoot/photon#filter-results-by-tags-and-values>`__
-  ``bbox``: a ``string`` with comma-separated values or ``list``
   containing `bounding box
   coordinates <https://github.com/komoot/photon#filter-results-by-bounding-box>`__

``Location`` object (or objects if you don't set limit=1) is generated
from the json returned and contains all the information you need: name,
state, street, city, osm attributes, extent\_from.latitude,
extent\_from.longitude, extent\_to.latitude, extent\_to.longitude ...

Reverse search
~~~~~~~~~~~~~~

Python Photon client allows you to make reverse search.

.. code:: py

    from pyphoton import Photon


    client = Photon()
    locations = client.reverse(latitude=52, longitude=10)

    for location in locations:
        print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))

You can pass to the ``reverse`` method the following parameters:

-  ``latitude`` and ``longitude``: use them to search using a geo
   position
-  ``limit``: limit number of results

Deal with errors
~~~~~~~~~~~~~~~~

If there's an error in your query, a ``PhotonException`` will be raised

.. code:: py

    from pyphoton import Photon
    from pyphoton.errors import PhotonException


    client = Photon()
    try:
        location = client.query('', limit=1)
    except PhotonException as ex:
        print (ex)

Run tests
---------

.. code:: sh

    pip install -r requirements-dev.txt
    make test

WIP Features
------------

-  Method to fetch `latest
   data <http://download1.graphhopper.com/public/>`__

.. |Latest Version| image:: https://img.shields.io/pypi/v/pyphoton.svg
   :target: https://pypi.python.org/pypi/pyphoton/
.. |codecov| image:: https://codecov.io/gh/astagi/pyphoton/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/astagi/pyphoton
.. |Build Status| image:: https://github.com/astagi/pyphoton/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/astagi/pyphoton/actions/workflows/ci.yml
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/astagi/pyphoton/blob/master/LICENSE
