import functools
import logging
import sys


logger = logging.getLogger(__name__)


def runnable(fn):
    @functools.wraps(fn)
    def wrapper():
        try:
            logger.info('Starting')
            fn()

        except KeyboardInterrupt:
            logger.info('Stopping')

        except Exception:
            logger.exception('Failure')
            sys.exit(1)

    return wrapper
