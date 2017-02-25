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

    JSON_FIELD_GROUP_NAME = "group"
    JSON_FIELD_OBJECT_NAME = "object"

    JSON_FIELD_TYPE = "type"
    JSON_FIELD_CURRENT_VALUE = "value"
    JSON_FIELD_MAXIMUM_VALUE = "max"
    JSON_FIELD_MINIMUM_VALUE = "min"
    JSON_FIELD_READONLY = "readOnly"

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
            data[cls.JSON_FIELD_GROUP_NAME],
            data[cls.JSON_FIELD_OBJECT_NAME],
            data[cls.JSON_FIELD_TYPE],
            data[cls.JSON_FIELD_CURRENT_VALUE],
            getValue(data, cls.JSON_FIELD_MAXIMUM_VALUE, None),
            getValue(data, cls.JSON_FIELD_MINIMUM_VALUE, None),
            getValue(data, cls.JSON_FIELD_READONLY, False)
        )

    def __init__(self, name, path, groupName, objectName, valueType,
                 currentValue, maxValue, minValue, readOnly):
        super(PropertyModel, self).__init__(name, path)

        typeOfValue = TypeModel.getType(valueType)

        self.__group = groupName
        self.__object = objectName
        self.__valueType = valueType

        if readOnly is None:
            readOnly = False

        if minValue is None and readOnly:
            minValue = maxValue

        if maxValue is None and readOnly:
            maxValue = minValue

        self.__valueObject = typeOfValue(
            currentValue,
            minValue,
            maxValue,
            readOnly=readOnly
        )

        assert isinstance(self.__valueObject, typeOfValue)
        self.__valueReadOnly = readOnly

        assert isinstance(self.groupName, six.string_types)
        assert isinstance(self.objectName, six.string_types)
        assert self.readOnly in (True, False)
        if self.readOnly:
            assert self.maximum == self.minimum

    def serialize(self):
        def setValue(dataSet, fieldName, value):
            dataSet[fieldName] = value

        data = super(PropertyModel, self).serialize()
        propertyData = {
            self.JSON_FIELD_GROUP_NAME: self.groupName,
            self.JSON_FIELD_OBJECT_NAME: self.objectName,
            self.JSON_FIELD_TYPE: self.valueType,
            self.JSON_FIELD_CURRENT_VALUE: self.value,
        }
        setValue(propertyData, self.JSON_FIELD_MAXIMUM_VALUE, self.maximum)
        setValue(propertyData, self.JSON_FIELD_MINIMUM_VALUE, self.minimum)
        setValue(propertyData, self.JSON_FIELD_READONLY, self.readOnly)

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

    @property
    def MIN_VALUE(self):
        return self.__valueObject.MIN_VALUE

    @property
    def MAX_VALUE(self):
        return self.__valueObject.MAX_VALUE

    @property
    def is_string(self):
        return self.__valueObject.is_string
