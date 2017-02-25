class JsonModel(object):
    """
    Basic JSON Model

    The basic JSON model is a list of requests.
    [
        {},
        ...
    ]
    """

    def __init__(self, json_data):
        self.data = json_data

    def validate(self):
        if isinstance(self.data, list):
            return True

        return False

    def entry(self):
        for value in self.data:
            yield value
