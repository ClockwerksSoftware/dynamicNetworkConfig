"""
Object Model: FS equivalent - file
"""
from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.base_model import BaseModel


class ObjectModel(BaseModel):
    """
    A model of a property collection

    An Object is a collection of properties that are highly related.

    .. note:: Properties are just the names of the sub-items
    """

    JSON_FIELD_GROUP_NAME = "group"
    JSON_FIELD_SUBPROPERTIES = "properties"

    @classmethod
    def deserialize(cls, data):
        base = BaseModel.deserialize(data)
        return cls(
            base.name,
            base.path,
            data[cls.JSON_FIELD_GROUP_NAME],
            data[cls.JSON_FIELD_SUBPROPERTIES]
        )

    def __init__(self, name, path, groupName, properties):
        super(ObjectModel, self).__init__(name, path)
        self.__group = groupName
        self.__properties = properties

        if not isinstance(self.__properties, (list, set)):
            raise errors.InvalidPropertyListing

        self.validate_group_name(self.groupName)

    def serialize(self):
        data = super(ObjectModel, self).serialize()
        data.update(
            {
                self.JSON_FIELD_GROUP_NAME: self.groupName,
                self.JSON_FIELD_SUBPROPERTIES: [
                    objectProperty
                    for objectProperty in self.properties
                ]
            }
        )
        return data

    @property
    def groupName(self):
        return self.__group

    @property
    def properties(self):
        for objectProperty in self.__properties:
            yield objectProperty
