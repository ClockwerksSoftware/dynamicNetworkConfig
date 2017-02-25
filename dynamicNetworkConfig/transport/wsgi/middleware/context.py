import dynamicNetworkConfig
import dynamicNetworkConfig.common.context as context
import dynamicNetworkConfig.common.local as local


class ContextObject(object):

    def __init__(self):
        self.datacenter = (
            dynamicNetworkConfig.config.api_configuration.datacenter.lower()
        )
        self._transaction = None
        self._authentication = None

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

    @property
    def authentication(self):
        return self._authentication

    @authentication.setter
    def authentication(self, value):
        self._authentication = value


class ContextMiddleware(object):

    TRANSACTION_CONTEXT = "TransactionContext"

    def process_request(self, request, response):
        dynamicNetworkConfig.context = ContextObject()

        dynamicNetworkConfig.context.transaction = context.RequestContext()
        setattr(
            local.store,
            ContextMiddleware.TRANSACTION_CONTEXT,
            dynamicNetworkConfig.context.transaction
        )

    def process_response(self, request, response, source):
        setattr(
            local.store,
            ContextMiddleware.TRANSACTION_CONTEXT,
            None
        )
        if dynamicNetworkConfig.context.transaction is not None:
            x = dynamicNetworkConfig.context.transaction
            dynamicNetworkConfig.context.transaction = None
            del x
