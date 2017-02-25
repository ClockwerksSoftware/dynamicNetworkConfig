import logging
from wsgiref import simple_server

import falcon

from dynamicNetworkConfig import conf
from dynamicNetworkConfig import model
from dynamicNetworkConfig.transport.wsgi import v1_0
from dynamicNetworkConfig.transport.wsgi import middleware


logger = logging.getLogger(__name__)


class Driver(object):

    def __init__(self):
        self.app = None
        self.init_routes()
        model.init_model()

    def init_middleware(self):
        middleware_list = [
            middleware.ContextMiddleware(),
            middleware.AuthenticationMiddleware()
        ]

        return middleware_list

    def init_routes(self):
        end_points = [
            ('/v1.0', v1_0.public_end_points())
        ]

        self.app = falcon.API(
            middleware=self.init_middleware()
        )

        for version_path, end_point in end_points:
            for route, resource in end_point:
                self.app.add_route(version_path + route,
                                   resource)

    def listen(self):
        logger.info('Server on {0}:{1}'
                    .format(conf.server.host,
                            conf.server.port))
        httpd = simple_server.make_server(conf.server.host,
                                          conf.server.port,
                                          self.app)
        httpd.serve_forever()
