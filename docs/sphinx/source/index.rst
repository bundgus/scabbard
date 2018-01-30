.. scabbard documentation master file, created by
   sphinx-quickstart on Mon Jan  1 19:09:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Scabbard's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

About
-----

Scabbard is a Pythonic client for the Sabre Dev Studio REST APIs.  With Scabbard, it
is not necessary to create extensive low-level boilerplate code before you can use each API call.
You can begin to interact with the Sabre Dev Studio APIs with as few as 3 lines of code.

A scabbard is a sheath for holding a sword, such as a sabre - https://en.wikipedia.org/wiki/Scabbard

.. image:: https://upload.wikimedia.org/wikipedia/commons/a/af/Arms_and_Armor.jpg
   :height: 170 px
   :width: 512 px
   :scale: 50 %
   :alt: Princely Mughal sabre with jewelled scabbard

Features
--------

Defined Scabbard REST endpoints can be reviewed in the SwaggerUI:
    https://bundgus.github.io/scabbard/SwaggerUI/index.html

Documentation
-------------

Sabre Dev Studio API Documentation:
    https://developer.sabre.com/docs/read/Home

Sabre Dev Studio REST API documentation:
    https://developer.sabre.com/docs/read/rest_apis/

    https://developer.sabre.com/io-docs

Scabbard docs:
    https://bundgus.github.io/scabbard/html/

Scabbard SwaggerUI:
    https://bundgus.github.io/scabbard/SwaggerUI/index.html

Scabbard GitHub Home:
    https://github.com/bundgus/scabbard

Scabbard PyPi Home:
    https://pypi.python.org/pypi/scabbard


Getting Started
---------------

(1)
You can register for a free Sabre Dev Studio account at the following URL:

https://developer.sabre.com/apps/mykeys

(2)
Install the scabbard library with pip.

.. code-block:: bash

    $ pip install scabbard

(3)
A file called api_connect_parameters.json must exist in the directory
in which python is run, with your Sabre Dev Studio clientID and clientSecret credentials.

api_connect_parameters.json

.. code-block:: javascript

    {
      "clientId": "zzzzzzzzzzzzzzzz",
      "clientSecret": "xxxxxxxx",
      "environment": "https://api.test.sabre.com",
      "group": "DEVCENTER",
      "domain": "EXT",
      "formatVersion": "V1"
    }


(4)
Run code to exercise the API.  For example:

example_V1ListsSupportedCountriesGet.py

.. code-block:: Python

    import scabbard

    client = scabbard.get_client()
    countries = client.Air_Utility.V1ListsSupportedCountriesGet(pointofsalecountry='NZ').result()

    print('PointOfSale')
    print(countries.PointOfSale)

    print('OriginCountries')
    for c in countries.OriginCountries:
        print(c.CountryCode, c.CountryName)

    print('DestinationCountries')
    for c in countries.DestinationCountries:
        print(c.CountryCode, c.CountryName)

    print('Links')
    for l in countries.Links:
        print(l.rel)
        print(l.href)

(5)
Run your python example.

.. code-block:: bash

    $ python example_V1ListsSupportedCountriesGet.py

    PointOfSale
    NZ
    OriginCountries
    AU Australia
    ID Indonesia
    IE Ireland
    NZ New Zealand
    TH Thailand
    GB United Kingdom
    DestinationCountries
    AU Australia
    FR France
    DE Germany
    HK Hong Kong
    IN India
    ID Indonesia
    IE Ireland
    MY Malaysia
    NL Netherlands
    NZ New Zealand
    PH Philippines
    SG Singapore
    TH Thailand
    GB United Kingdom
    US United States
    Links
    self
    https://api.test.sabre.com/v1/lists/supported/countries?pointofsalecountry=NZ
    linkTemplate
    https://api.test.sabre.com/v1/lists/supported/countries?pointofsalecountry=<pointofsalecountry>


Installation
------------

.. code-block:: bash

    $ pip install scabbard

Run Pytests
-----------

.. code-block:: bash

    $ python -m pytest

License
-------

Copyright (c) 2018, Mark Bundgus. All rights reserved.

* not a Sabre provided or supported software library
* all referenced Sabre content and services are the property of Sabre

Scabbard is licensed with a `BSD 3-Clause
License <http://opensource.org/licenses/BSD-3-Clause>`__.
