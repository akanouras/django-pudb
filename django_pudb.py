# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http import Http404

pudb = None  # Silence pyflakes


class PudbMiddleware(object):
    def __init__(self):
        if not getattr(settings, 'DEBUG', False):
            raise MiddlewareNotUsed

        # Hack alert :)
        import traceback
        if '/threading.py' in traceback.extract_stack()[0][0]:
            print('PudbMiddleware: Threading not (yet) supported, unloading myself.')
            raise MiddlewareNotUsed

        try:
            global pudb
            import pudb
            assert pudb  # Silence pyflakes
        except ImportError:
            print('PudbMiddleware: Could not import pudb, unloading myself.')
            raise MiddlewareNotUsed

        print('PudbMiddleware: DEBUG enabled and pudb found, intercepting all uncaught exceptions.')

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return
        print('PudbMiddleware: activating on "{0}"'.format(repr(exception)))
        pudb.post_mortem()
