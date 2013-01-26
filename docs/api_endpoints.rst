OpenPortfolio API Endpoint Documentation
========================================

This is a simple proof-of-concept REST-ful API for an open e-portfolio for use
by trainee doctors within the NHS.

For speed we use Basic HTTP Authentication (see:
https://en.wikipedia.org/wiki/Basic_access_authentication). To make sure the
credentials cannot be intercepted we enforce SSL/TLS so the connection is
encrypted.

Currently the API is hosted here:

https://o-portfolio-api.herokuapp.com/

Endpoints
=========

`/register`
+++++++++++

POST
----

Creates a new user. Payload should conform to the following::

    {
        'first_name': 'Fred',
        'last_name': 'Bloggs',
        'email': 'fred@bloggs.com',
        'password': 'SEKRET1234'
    }

`/users`
++++++++

PUT
---

Allows an authenticated user to change their settings. Payload must conform to
the following::

    {
        'first_name': 'Fred',
        'last_name': 'Bloggs',
        'email': 'fred@bloggs.com',
        'password': 'SEKRET1234'
    }

(Only one or more of the above fields is actually needed).

GET
---

Returns the user's `first_name`, `last_name` and `email fields` in a JSON
object.


`/entries`
++++++++++

POST
----

Creates a new entry in the authenticated user's portfolio. Payload must
conform to the following::

    {
        title: 'DOPS assessment',
        description: 'iv cannulation',
        reflection: 'Preparation was good, vein identified. Pt not adequately warned and moved so I missed. Will learn from this and communicate better.',
        occurred_at: '2013-01-26T08:19Z'
    }

(Nota Bene: the `occurred_at` value must confirm to ISO8601 - viz: https://en.wikipedia.org/wiki/ISO_8601)

`/entries/<ID>`
+++++++++++++++

PUT
---

Updates the fields in a specific entry for the authenticated user. Payload
must conform to the following::

    {
        title: 'DOPS assessment',
        description: 'iv cannulation',
        reflection: 'Preparation was good, vein identified. Pt not adequately warned and moved so I missed. Will learn from this and communicate better.',
        occurred_at: '2013-01-26T08:19Z'
    }

(Only one or more of the above fields is actually needed).

(Nota Bene: the `occurred_at` value must confirm to ISO8601 - viz: https://en.wikipedia.org/wiki/ISO_8601)

GET
---

Returns a JSON representation of the referenced entry for an authenticated
user.

DELETE
------

Removes an entry from the system for an authenticated user.
