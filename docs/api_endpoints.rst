OpenPortfolio API Endpoint Documentation
========================================

This is a simple proof-of-concept REST-ful API for an open e-portfolio for use
by trainee doctors within the NHS.

We use token based sessions for authentication. The token should always be
sent in request headers using the ``Authorization`` key and the string literal
``Token<space>`` prefixing your token (see the docs for the ``login`` endpoint
below for starting a session).

Currently the API is hosted here:

https://o-portfolio-api.herokuapp.com/

Endpoints
=========

`/login`
++++++++

POST
----

Creates a new session given the user's credentials. Payload should conform to
the following::

    {
        'username': 'fred@blogs.com',
        'password': 'SEKRET1234'
    }

Remember! The username must be the user's email address.

The endpoint will respond with a JSON object containing the token::

    {
        'token': 'averylontokenstringfoobarbaz'
    }

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
