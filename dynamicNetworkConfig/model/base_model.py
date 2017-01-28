import re

import six

from dynamicNetworkConfig.common import errors


class BaseModel(object):
    """
    The primal descriptions
    """

    PATH_SEPARATOR = "/"
    PATH_ROOT = "/"

    NAME_MATCHER = re.compile("^\w*$")
    GROUP_NAME_MATCHER = re.compile("^\w*$")
    OBJECT_NAME_MATCHER = re.compile("^\w*$")

    @classmethod
    def validate_name(cls, name):
        if not cls.NAME_MATCHER.match(name):
            raise errors.InvalidName(
                "Invalid Name".format(
                    name
                )
            )

    @classmethod
    def validate_group_name(cls, name):
        if not cls.GROUP_NAME_MATCHER.match(name):
            raise errors.InvalidGroupName(
                "Invalid Group Name - {0}".format(
                    name
                )
            )

    @classmethod
    def validate_object_name(cls, name):
        if not cls.OBJECT_NAME_MATCHER.match(name):
            raise errors.InvalidObjectName(
                "Invalid Object Name - {0}".format(
                    name
                )
            )

    @classmethod
    def validate_path(cls, path):
        if not path.startswith(cls.PATH_SEPARATOR):
            raise errors.InvalidPath(
                "Path does not start with the root"
            )

        groups = path.split(cls.PATH_SEPARATOR)
        groups.remove('')

        for group_name in groups:
            try:
                cls.validate_group_name(group_name)
            except errors.InvalidGroupName:
                raise errors.InvalidPath(
                    "Path contains invalid group name {0}".format(
                        group_name
                    )
                )

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

        assert isinstance(self.name, six.string_types)
        assert isinstance(self.path, six.string_types)

        self.validate_name(self.name)
        self.validate_path(self.path)

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
