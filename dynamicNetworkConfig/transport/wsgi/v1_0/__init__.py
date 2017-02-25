from dynamicNetworkConfig.transport.wsgi.v1_0 import root
from dynamicNetworkConfig.transport.wsgi.v1_0 import groups
from dynamicNetworkConfig.transport.wsgi.v1_0 import objects
from dynamicNetworkConfig.transport.wsgi.v1_0 import properties
from dynamicNetworkConfig.transport.wsgi.v1_0 import health
from dynamicNetworkConfig.transport.wsgi.v1_0 import home
from dynamicNetworkConfig.transport.wsgi.v1_0 import ping


def public_end_points():
    """
    """

    return [
        ('/', home.Resource()),
        ('/health', health.Resource()),
        ('/ping', ping.Resource()),
        ('/config', root.Resource()),
        ('/groups', groups.Resource()),
        ('/objects', objects.Resource()),
        ('/properties', properties.Resource())
    ]
