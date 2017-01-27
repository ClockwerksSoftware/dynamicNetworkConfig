import six


class BaseModel(object):
    """
    The primal descriptions
    """

    # JSON Fields for serialization support
    JSON_FIELD_NAME = "name"
    JSON_FIELD_PATH = "path"

    @classmethod
    def deserialize(cls, json_data):
        """
        Deserialize the provided `dict` into the BaseModel class

        .. note:: json_data is a Python `dict` and may contain other
            key-value pairs.
        """
        return cls(
            json_data[cls.JSON_FIELD_NAME],
            json_data[cls.JSON_FIELD_PATH]
        )

    def __init__(self, name, path):
        self.__name = name
        self.__path = path

        assert isinstance(self.name, six.text_type)
        assert isinstance(self.path, six.text_type)

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path

    def serialize(self):
        return {
            self.JSON_FIELD_NAME: self.name,
            self.JSON_FIELD_PATH: self.path
        }
