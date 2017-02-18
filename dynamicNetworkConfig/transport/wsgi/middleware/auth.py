import dynamicNetworkConfig.common.local


class AuthenticationObject(object):

    def __init__(self, name, token):
        self.name = name
        self._auth_token = token

    @property
    def authToken(self):
        return self._auth_token


class AuthenticationMiddleware(object):

    AUTHENICATION_CONTEXT = "AuthenicationContext"

    def process_request(self, request, response):
        auth_token = request.get_header(
            'x-auth-token',
            required=True
        )

        dynamicNetworkConfig.context.authentication = AuthenticationObject(
            'Authentication Context',
            auth_token
        )
        setattr(
            local.store,
            AuthenticationMiddleware.AUTHENICATION_CONTEXT,
            dynamicNetworkConfig.context.authentication
        )

    def process_response(self, request, response, source):
        setattr(
            local.store,
            AuthenticationMiddleware.AUTHENICATION_CONTEXT,
            None
        )
        if dynamicNetworkConfig.context.authenciation is not None:
            x = dynamicNetworkConfig.context.authenciation
            dynamicNetworkConfig.context.authenciation = None
            del x
