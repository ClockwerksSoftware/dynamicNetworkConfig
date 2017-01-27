import dynamicNetworkConfig.server as cli
from dynamicNetworkConfig.transport.wsgi.driver import Driver


@cli.runnable
def run():
    app_container = Driver()
    app_container.listen()
