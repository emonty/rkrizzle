Rkrizzle: HTTP for People
=========================

Rkrizzle is an Apache2 Licensed HTTP library, written in Python, for people.
It is a fork of the amazing requests library with two major differences:

- No vendored libraries
- Honors and uses OS System CA Bundles

Rkrizzle aims to be easy to be used both from an OS distro perspective, and
for direct python developers working from PyPI, and to do what people expect
of a key system library - such as playing nicely with the rest of the system.

If you're curious as to why we forked and didn't just patch requests itself,
please see `Kenneth's Views <https://github.com/kennethreitz/requests/pull/1812#issuecomment-30854316>`_
on the subject of vendoring. The disagreement is intractable.

Rkrizzle has every intention of maintaining API compatibility with requests.
It is a completely fair choice for the requests authors to choose to bundle
libraries and CA Bundles. That doesn't work for us, so we're doing this.
Hopefully we can all get along.

Using
-----

Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python's builtin urllib2 module provides most of
the HTTP capabilities you should need, but the api is thoroughly broken.
It requires an enormous amount of work (even method overrides) to
perform the simplest of tasks.

Things shouldn't be this way. Not in Python.

.. code-block:: python

    >>> r = rkrizzle.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

See `the same code, without Rkrizzle <https://gist.github.com/973705>`_.

Rkrizzle allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://pypi.python.org/pypi/urllib3>`_, but it does all the hard work and
crazy hacks for you.


Features
--------

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Rkrizzle with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Unicode Response Bodies
- Multipart File Uploads
- Connection Timeouts
- Thread-safety
- HTTP(S) proxy support


Installation
------------

To install Rkrizzle, simply:

.. code-block:: bash

    $ pip install rkrizzle


Documentation
-------------

Documentation is available at http://rkrizzle.readthedocs.org/.
