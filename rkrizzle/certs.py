# Copyright: (c) 2015 by IBM Corp.
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
certs.py
~~~~~~~~

This module returns the preferred default CA certificate bundle.
"""

import platform

_LINUX_LOCATION = '/etc/pki/tls/certs/ca-bundle.crt'


def where():
    """Return the preferred certificate bundle."""
    if platform.linux_distribution()[0]:
        return _LINUX_LOCATION
    else:
        import certifi
        return certifi.where()

if __name__ == '__main__':
    print(where())
