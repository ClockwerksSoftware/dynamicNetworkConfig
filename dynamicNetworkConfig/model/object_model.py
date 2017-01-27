"""
Object Model: FS equivalent - file
"""
import six

from dynamicNetworkConfig.model.base_model import BaseModel


class ObjectModel(BaseModel):
    """
    A model of a property collection

    An Object is a collection of properties that are highly related.

    .. note:: Properties are just the names of the sub-items
    """

    FIELD_GROUP_NAME = "group"
    FIELD_SUBPROPERTIES = "properties"

    @classmethod
    def deserialize(cls, data):
        base = BaseModel.deserialize(data)
        return cls(
            base.name,
            base.path,
            data[cls.FIELD_GROUP_NAME],
            data[cls.FIELD_SUBPROPERTIES]
        )

    def __init__(self, name, path, groupName, properties):
        super(self, ObjectModel).__init__(name, path)
        self.__group = groupName
        self.__properties = properties

        assert isinstance(self.properties, (list, set))
        assert isinstance(self.groupName, six.text_type)

    def serialize(self):
        data = super(self, ObjectModel).serialize()
        data.update(
            {
                self.FIELD_GROUP_NAME: self.groupName,
                self.FIELD_SUBPROPERTIES: [
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
