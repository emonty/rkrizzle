.. _api:

Developer Interface
===================

.. module:: rkrizzle

This part of the documentation covers all the interfaces of Rkrizzle. For
parts where Rkrizzle depends on external libraries, we document the most
important right here and provide links to the canonical documentation.


Main Interface
--------------

All of Requests' functionality can be accessed by these 7 methods.
They all return an instance of the :class:`Response <Response>` object.

.. autofunction:: request

.. autofunction:: head
.. autofunction:: get
.. autofunction:: post
.. autofunction:: put
.. autofunction:: patch
.. autofunction:: delete


Lower-Level Classes
~~~~~~~~~~~~~~~~~~~

.. autoclass:: rkrizzle.Request
   :inherited-members:

.. autoclass:: Response
   :inherited-members:

Request Rkrizzle
----------------

.. autoclass:: Session
   :inherited-members:

.. autoclass:: rkrizzle.adapters.HTTPAdapter
   :inherited-members:

Authentication
--------------

.. autoclass:: rkrizzle.auth.AuthBase
.. autoclass:: rkrizzle.auth.HTTPBasicAuth
.. autoclass:: rkrizzle.auth.HTTPProxyAuth
.. autoclass:: rkrizzle.auth.HTTPDigestAuth

Exceptions
~~~~~~~~~~

.. autoexception:: rkrizzle.exceptions.RequestException
.. autoexception:: rkrizzle.exceptions.ConnectionError
.. autoexception:: rkrizzle.exceptions.HTTPError
.. autoexception:: rkrizzle.exceptions.URLRequired
.. autoexception:: rkrizzle.exceptions.TooManyRedirects
.. autoexception:: rkrizzle.exceptions.ConnectTimeout
.. autoexception:: rkrizzle.exceptions.ReadTimeout
.. autoexception:: rkrizzle.exceptions.Timeout


Status Code Lookup
~~~~~~~~~~~~~~~~~~

.. autofunction:: rkrizzle.codes

::

    >>> rkrizzle.codes['temporary_redirect']
    307

    >>> rkrizzle.codes.teapot
    418

    >>> rkrizzle.codes['\o/']
    200

.. _api-cookies:

Cookies
~~~~~~~

.. autofunction:: rkrizzle.utils.dict_from_cookiejar
.. autofunction:: rkrizzle.utils.cookiejar_from_dict
.. autofunction:: rkrizzle.utils.add_dict_to_cookiejar

.. autoclass:: rkrizzle.cookies.RequestsCookieJar
   :inherited-members:

.. autoclass:: rkrizzle.cookies.CookieConflictError
   :inherited-members:


Encodings
~~~~~~~~~

.. autofunction:: rkrizzle.utils.get_encodings_from_content
.. autofunction:: rkrizzle.utils.get_encoding_from_headers
.. autofunction:: rkrizzle.utils.get_unicode_from_response


Classes
~~~~~~~

.. autoclass:: rkrizzle.Response
   :inherited-members:

.. autoclass:: rkrizzle.Request
   :inherited-members:

.. autoclass:: rkrizzle.PreparedRequest
   :inherited-members:

.. _sessionapi:

.. autoclass:: rkrizzle.Session
   :inherited-members:

.. autoclass:: rkrizzle.adapters.HTTPAdapter
   :inherited-members:


Migrating to 1.x
----------------

This section details the main differences between 0.x and 1.x and is meant
to ease the pain of upgrading.


API Changes
~~~~~~~~~~~

* ``Response.json`` is now a callable and not a property of a response.

  ::

      import rkrizzle
      r = rkrizzle.get('https://github.com/timeline.json')
      r.json()   # This *call* raises an exception if JSON decoding fails

* The ``Session`` API has changed. Rkrizzle objects no longer take parameters.
  ``Session`` is also now capitalized, but it can still be
  instantiated with a lowercase ``session`` for backwards compatibility.

  ::

      s = rkrizzle.Session()    # formerly, session took parameters
      s.auth = auth
      s.headers.update(headers)
      r = s.get('http://httpbin.org/headers')

* All request hooks have been removed except 'response'.

* Authentication helpers have been broken out into separate modules. See
  requests-oauthlib_ and requests-kerberos_.

.. _requests-oauthlib: https://github.com/requests/requests-oauthlib
.. _requests-kerberos: https://github.com/requests/requests-kerberos

* The parameter for streaming requests was changed from ``prefetch`` to
  ``stream`` and the logic was inverted. In addition, ``stream`` is now
  required for raw response reading.

  ::

      # in 0.x, passing prefetch=False would accomplish the same thing
      r = rkrizzle.get('https://github.com/timeline.json', stream=True)
      for chunk in r.iter_content(8192):
          ...

* The ``config`` parameter to the requests method has been removed. Some of
  these options are now configured on a ``Session`` such as keep-alive and
  maximum number of redirects. The verbosity option should be handled by
  configuring logging.

  ::

      import rkrizzle
      import logging

      # these two lines enable debugging at httplib level (requests->urllib3->httplib)
      # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
      # the only thing missing will be the response.body which is not logged.
      import httplib
      httplib.HTTPConnection.debuglevel = 1

      logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from rkrizzle
      logging.getLogger().setLevel(logging.DEBUG)
      requests_log = logging.getLogger("urllib3")
      requests_log.setLevel(logging.DEBUG)
      requests_log.propagate = True

      rkrizzle.get('http://httpbin.org/headers')
