from dynamicNetworkConfig.transport.wsgi import helpers


class Resource(object):

    def on_head(self, request, response):
        data = get_json(request, "HEAD")

    def on_get(self, request, response):
        data = get_json(request, "GET")

    def on_put(self, request, response):
        data = get_json(request, "PUT")

    def on_post(self, request, response):
        data = get_json(request, "POST")

    def on_delete(self, request, response):
        data = get_json(request, "DELETE")
