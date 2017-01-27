import falcon
from falcon import http_error
from falcon import status as http_status


class NoDataError(falcon.HTTPBadRequest):

    TITLE = u'No Content'

    def __init__(self, description):
        super(NoDataError, self).__init__(self.TITLE, description)


class TooLittleDataError(falcon.HTTPBadRequest):

    TITLE = u'Bad Content Length'

    def __init__(self, description):
        super(TooLittleDataError, self).__init__(self.TITLE, description)


class UnableToDecodeDataError(falcon.HTTPBadRequest):

    TITLE = u'Invalid Content Format'

    def __init__(self, description):
        super(UnableToDecodeDataError, self).__init__(self.TITLE, description)


class InvalidJsonError(falcon.HTTPBadRequest):

    TITLE = u'Invalid JSON Content'

    def __init__(self, description):
        super(InvalidJsonError, self).__init__(self.TITLE, description)
