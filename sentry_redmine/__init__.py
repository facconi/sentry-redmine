"""
sentry_redmine
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Aaditya Sood, Idea Device
:license: BSD, see LICENSE for more details.
"""

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-redmine').version
except Exception, e:
    VERSION = 'unknown'
