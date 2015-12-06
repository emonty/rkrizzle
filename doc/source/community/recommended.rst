.. _recommended:

Recommended Packages and Extensions
===================================

Rkrizzle has a great variety of powerful and useful third-party extensions.
This page provides an overview of some of the best of them.

CacheControl
------------

`CacheControl`_ is an extension that adds a full HTTP cache to Rkrizzle. This
makes your web requests substantially more efficient, and should be used
whenever you're making a lot of web requests.

.. _CacheControl: https://cachecontrol.readthedocs.org/en/latest/


Requests-OAuthlib
-----------------

`requests-oauthlib`_ makes it possible to do the OAuth dance from Rkrizzle
automatically. This is useful for the large number of websites that use OAuth
to provide authentication. It also provides a lot of tweaks that handle ways
that specific OAuth providers differ from the standard specifications.

.. _requests-oauthlib: https://requests-oauthlib.readthedocs.org/en/latest/


Betamax
-------

`Betamax`_ records your HTTP interactions so the NSA does not have to.
A VCR imitation designed only for Python-Requests.

.. _betamax: https://github.com/sigmavirus24/betamax
