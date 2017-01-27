from dynamicNetworkConfig.transport.wsgi.driver import Driver


app_container = Driver()
app = app_container.app
