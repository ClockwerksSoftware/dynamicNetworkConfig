import unittest

import falcon
from falcon import testing as ftest
import six

from dynamicNetworkConfig.transport.wsgi.driver import Driver


class DummyContext():
    pass


def setUp():
    pass


def tearDown():
    pass


class TestBase(unittest.TestCase):

    def setUp(self):
        super(TestBase, self).setUp()

        import dynamicNetworkConfig
        dynamicNetworkConfig.context = DummyContext()

        self.app = Driver().app
        self.srmock = ftest.StartResponseMock()
        self.headers = {}

    def tearDown(self):
        super(TestBase, self).tearDown()

        import dynamicNetworkConfig
        dynamicNetworkConfig.context = None

    def simulate_request(self, method, path, **kwargs):
        self.srmock = ftest.StartResponseMock()
        headers = kwargs.get('headers', self.headers).copy()
        kwargs['method'] = method
        kwargs['headers'] = headers
        return self.app(
            ftest.create_environ(
                path=path,
                protocol='HTTP/1.1',
                **kwargs
            ),
            self.srmock
        )

    def simulate_head(self, *args, **kwargs):
        return self.simulate_request('HEAD', *args, **kwargs)

    def simulate_get(self, *args, **kwargs):
        return self.simulate_request('GET', *args, **kwargs)

    def simulate_put(self, *args, **kwargs):
        return self.simulate_request('PUT', *args, **kwargs)

    def simulate_post(self, *args, **kwargs):
        return self.simulate_request('POST', *args, **kwargs)

    def simulate_delete(self, *args, **kwargs):
        return self.simulate_request('DELETE', *args, **kwargs)

    def simulate_options(self, *args, **kwargs):
        return self.simulate_request('OPTIONS', *args, **kwargs)

    def simulate_patch(self, *args, **kwargs):
        return self.simulate_request('PATCH', *args, **kwargs)
