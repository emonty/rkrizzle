# Copyright: (c) 2015 by Kenneth Reitz.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Rkrizzle HTTP library
~~~~~~~~~~~~~~~~~~~~~

Rkrizzle is an HTTP library, written in Python, for people. Basic GET
usage:

   >>> import rkrizzle
   >>> r = rkrizzle.get('https://www.python.org')
   >>> r.status_code
   200
   >>> 'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = rkrizzle.post('http://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key2": "value2",
       "key1": "value1"
     },
     ...
   }

The other HTTP methods are supported - see `rkrizzle.api`. Full documentation
is at <http://rkrizzle.readthedocs.org>

:license: Apache 2.0, see LICENSE for more details.

"""
import pbr.version

__title__ = 'rkrizzle'
__version__ = pbr.version.VersionInfo('rkrizzle').version_string()
__build__ = pbr.version.VersionInfo('rkrizzle').release_string()
__author__ = 'Kenneth Reitz'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 Kenneth Reitz'

from urllib3.contrib import pyopenssl
pyopenssl.inject_into_urllib3()
import urllib3.exceptions

__all__ = (
    'PreparedRequest',
    'Request',
    'Response',
    'delete',
    'get',
    'head',
    'options',
    'patch',
    'post',
    'put',
    'request',
    'utils',
)
from . import utils
from .models import Request, Response, PreparedRequest
from .api import request, get, head, post, patch, put, delete, options
from .sessions import session, Session
from .status_codes import codes
from .exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError,
    FileModeWarning,
)

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

import warnings

# FileModeWarnings go off per the default.
warnings.simplefilter('default', FileModeWarning, append=True)

# this urllib3 warning is evil, as it expresses a warning about a cert
# that quite literally the user cannot do anything about
warnings.filterwarnings(
    'ignore', category=urllib3.exceptions.SubjectAltNameWarning)

# this warning tells you to use a newer python, which may not be a choice
# for you, or to use pyOpenSSL, which we always use in rkrizzle
warnings.filterwarnings(
    'ignore', category=urllib3.exceptions.InsecurePlatformWarning)

# There are two paths to SSL in rkrizzle - either you explicitly said
# "I am making an insecure connection" - in which case the warning here
# is just annoying and not helping anything, OR you have not said it's
# insecure in which case we're going to hard-fail.
warnings.filterwarnings(
    'ignore', category=urllib3.exceptions.InsecureRequestWarning)
