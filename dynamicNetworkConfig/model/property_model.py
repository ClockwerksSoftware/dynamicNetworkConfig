"""
Property Model: FS equivalent - file contents
"""
import six

from dynamicNetworkConfig.model.base_model import BaseModel
import dynamicNetworkConfig.model.type_model as TypeModel


class PropertyModel(BaseModel):
    """
    A model of a specific property
    """

    FIELD_GROUP_NAME = "group"
    FIELD_OBJECT_NAME = "object"

    FIELD_TYPE = "type"
    FIELD_CURRENT_VALUE = "value"
    FIELD_MAXIMUM_VALUE = "max"
    FIELD_MINIMUM_VALUE = "min"
    FIELD_READONLY = "readOnly"

    SUPPORTED_TYPES = tuple(TypeModel.type_list)

    @classmethod
    def deserialize(cls, data):
        def getValue(dataSet, fieldName, defaultValue):
            if fieldName in dataSet:
                return dataSet[fieldName]
            else:
                return defaultValue

        base = BaseModel.deserialize(data)
        return cls(
            base.name,
            base.path,
            data[cls.FIELD_GROUP_NAME],
            data[cls.FIELD_OBJECT_NAME],
            data[cls.FIELD_TYPE],
            data[cls.FIELD_CURRENT_VALUE],
            getValue(data, cls.FIELD_MAXIMUM_VALUE, None),
            getValue(data, cls.FIELD_MINIMUM_VALUE, None),
            getValue(data, cls.FIELD_READONLY, True)
        )

    def __init__(self, name, path, groupName, objectName, valueType,
                 currentValue, maxValue, minValue, readOnly):
        typeOfValue = TypeModel.getType(valueType)

        super(self, PropertyModel).__init__(name, path)
        self.__group = groupName
        self.__object = objectName
        self.__valueType = valueType,

        self.__valueObject = typeOfValue(
            currentValue,
            minValue,
            maxValue
        )
        self.__valueReadOnly = readOnly

        assert isinstance(self.groupName, six.text_type)
        assert isinstance(self.objectName, six.text_type)
        assert isinstance(self.valueType, self.SUPPORTED_TYPES)
        assert isinstance(self.value, six.text_type)
        assert isinstance(self.maximum, type(self.valueType))
        assert isinstance(self.minimum, type(self.valueType))
        assert self.readOnly in (True, False)

    def serialize(self):
        def setValue(dataSet, fieldName, value):
            if value is not None:
                dataSet[fieldName] = value

        data = super(self, PropertyModel).serialize()
        propertyData = {
            self.FIELD_GROUP_NAME: self.groupName,
            self.FIELD_OBJECT_NAME: self.objectName,
            self.FIELD_TYPE: self.valueType,
            self.FIELD_CURRENT_VALUE: self.value,
        }
        setValue(propertyValue, self.FIELD_MAXIMUM_VALUE, self.maximum)
        setValue(propertyValue, self.FIELD_MINIMUM_VALUE, self.minimum)
        setValue(propertyValue, self.FIELD_READONLY, self.readOnly)

        data.update(propertyData)
        return data

    @property
    def groupName(self):
        return self.__group

    @property
    def objectName(self):
        return self.__object

    @property
    def valueType(self):
        return self.__valueType

    @property
    def value(self):
        return self.__valueObject.value

    @property
    def maximum(self):
        return self.__valueObject.maximum

    @property
    def minimum(self):
        return self.__valueObject.minimum

    @property
    def readOnly(self):
        return self.__valueReadOnly
