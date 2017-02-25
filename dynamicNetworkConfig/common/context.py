import uuid


class RequestContext(object):

    def __init__(self):
        self.request_id = 'dnc-req-{0}'.format(uuid.uuid4())
