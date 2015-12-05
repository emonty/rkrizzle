.. _faq:

Frequently Asked Questions
==========================

This part of the documentation answers common questions about Rkrizzle.

Encoded Data?
-------------

Rkrizzle automatically decompresses gzip-encoded responses, and does
its best to decode response content to unicode when possible.

You can get direct access to the raw response (and even the socket),
if needed as well.


Custom User-Agents?
-------------------

Rkrizzle allows you to easily override User-Agent strings, along with
any other HTTP Header.


Why not Requests
----------------

In a world of Linux distros and package management, and where even Python
has working dependency management, vendoring software is a bad practice. It's
expedient for the author, but for consumers of libraries it's a nightmare.
When requests bundles urllib3 and there is then a security vulnerability in
urllib3, a user is not taken care of if they update urllib3. We have the
technology to solve this - it's on us as developers of software to take care
of our users and reduce, where we can, their pain in attempting to.

Similarly with CA Bundles. EVERYONE's operating system has trusted bundles
installed, and system-level facilities for adding additional CA Bundles. By
bundling a CA Bundle into requests, the library defeats all of the work put
in to maintaining up to date SSL infrastructure.

For the authors of Rkrizzle, these two justify making a fork. While we're at
it though, we also find the requests practice of throwing warnings that a
user cannot do anything about to be more than annoying.

We're sorry it had to come to this though.

Why not Httplib2?
-----------------

Chris Adams gave an excellent summary about requests that should be
equally as relevant on
`Hacker News <http://news.ycombinator.com/item?id=2884406>`_:

    httplib2 is part of why you should use requests: it's far more respectable
    as a client but not as well documented and it still takes way too much code
    for basic operations. I appreciate what httplib2 is trying to do, that
    there's a ton of hard low-level annoyances in building a modern HTTP
    client, but really, just use requests instead. Kenneth Reitz is very
    motivated and he gets the degree to which simple things should be simple
    whereas httplib2 feels more like an academic exercise than something
    people should use to build production systems[1].

    Disclosure: I'm listed in the requests AUTHORS file but can claim credit
    for, oh, about 0.0001% of the awesomeness.

    1. http://code.google.com/p/httplib2/issues/detail?id=96 is a good example:
    an annoying bug which affect many people, there was a fix available for
    months, which worked great when I applied it in a fork and pounded a couple
    TB of data through it, but it took over a year to make it into trunk and
    even longer to make it onto PyPI where any other project which required "
    httplib2" would get the working version.


Python 3 Support?
-----------------

Yes! Here's a list of Python platforms that are officially
supported:

* Python 2.7
* Python 3.1
* Python 3.2
* Python 3.3
* Python 3.4
* PyPy 1.9
* PyPy 2.2

What are "hostname doesn't match" errors?
-----------------------------------------

These errors occur when :ref:`SSL certificate verification <verification>`
fails to match the certificate the server responds with to the hostname
Rkrizzle thinks it's contacting. If you're certain the server's SSL setup is
correct (for example, because you can visit the site with your browser) and
you're using Python 2.6 or 2.7, a possible explanation is that you need
Server-Name-Indication.

`Server-Name-Indication`_, or SNI, is an official extension to SSL where the
client tells the server what hostname it is contacting. This is important
when servers are using `Virtual Hosting`_. When such servers are hosting
more than one SSL site they need to be able to return the appropriate
certificate based on the hostname the client is connecting to.

Python3 and Python 2.7.9+ include native support for SNI in their SSL modules.
For information on using SNI with Rkrizzle on Python < 2.7.9 refer to this
`Stack Overflow answer`_.

.. _`Server-Name-Indication`: https://en.wikipedia.org/wiki/Server_Name_Indication
.. _`virtual hosting`: https://en.wikipedia.org/wiki/Virtual_hosting
.. _`Stack Overflow answer`: https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484
