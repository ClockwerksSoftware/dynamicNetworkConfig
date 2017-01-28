"""
Group Model: FS equivalent - directory
"""
from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.base_model import BaseModel


class GroupModel(BaseModel):
    """
    A model of a group collection

    A Group is a collection of (a) groups and (b) objects.

    .. note:: Groups and Objects are just the names of the sub-items
    """

    JSON_FIELD_SUBGROUPS = "groups"
    JSON_FIELD_SUBOBJECTS = "objects"

    ROOT_PATH = "/"

    @classmethod
    def deserialize(cls, data):
        base = BaseModel.deserialize(data)
        return cls(
            base.name,
            base.path,
            data[cls.JSON_FIELD_SUBGROUPS],
            data[cls.JSON_FIELD_SUBOBJECTS]
        )

    def __init__(self, name, path, groups, objects):
        super(GroupModel, self).__init__(name, path)
        self.__subgroups = groups
        self.__objects = objects

        if not isinstance(self.__subgroups, (list, set)):
            raise errors.InvalidGroupListing

        if not isinstance(self.__objects, (list, set)):
            raise errors.InvalidObjectListing


    def serialize(self):
        data = super(GroupModel, self).serialize()
        data.update(
            {
                self.JSON_FIELD_SUBGROUPS: [
                    subgroup
                    for subgroup in self.groups
                ],
                self.JSON_FIELD_SUBOBJECTS: [
                    subobject
                    for subobject in self.objects
                ]
            }
        )
        return data

    @property
    def is_root(self):
        if self.path == self.ROOT_PATH:
            return True

        return False

    @property
    def groups(self):
        for subgroup in self.__subgroups:
            yield subgroup

    @property
    def objects(self):
        for subobject in self.__objects:
            yield subobject
