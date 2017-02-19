import ddt

import six

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.property_model import PropertyModel


@ddt.ddt
class TestModelProperties(TestBase):

    def setUp(self):
        super(TestModelProperties, self).setUp()
        self.name = six.text_type('myProperty')
        self.objectName = six.text_type('myObject')
        self.groupName = six.text_type('myGroup')
        self.path = six.text_type('/some/path/to/the/group')

    def tearDown(self):
        super(TestModelProperties, self).tearDown()

    @ddt.data(
        (six.text_type('float'), 5.0, 10.0, -10.0, False, False),
        (six.text_type('float'), 5.0, 5.0, 5.0, True, False),
        (six.text_type('integer'), 5, 10, -10, False, False),
        (six.text_type('integer'), 5, 5, 5, True, False),
        (six.text_type('unsignedInteger'), 5, 10, 1, False, False),
        (six.text_type('unsignedInteger'), 5, 5, 5, True, False),
        (six.text_type('string'), six.text_type('hello'), 10, 4, False, True),
        (six.text_type('string'), six.text_type('hello'), 5, 5, True, True)
    )
    @ddt.unpack
    def test_instantiation(self,
            valueType, currentValue, maxValue, minValue, readOnly,
            is_string):
        pm = PropertyModel(
            self.name, self.path, self.groupName, self.objectName,
            valueType, currentValue, maxValue, minValue, readOnly
        )
        self.assertEqual(pm.name, self.name)
        self.assertEqual(pm.path, self.path)
        self.assertEqual(pm.groupName, self.groupName)
        self.assertEqual(pm.objectName, self.objectName)
        self.assertEqual(pm.valueType, valueType)
        self.assertEqual(pm.value, currentValue)
        self.assertEqual(pm.maximum, maxValue)
        self.assertEqual(pm.minimum, minValue)
        self.assertEqual(pm.readOnly, readOnly)
        self.assertEqual(pm.is_string, is_string)

    @ddt.data(
        (six.text_type('float'), 5.0, 10.0, -10.0, False),
        (six.text_type('float'), 5.0, 5.0, 5.0, True),
        (six.text_type('integer'), 5, 10, -10, False),
        (six.text_type('integer'), 5, 5, 5, True),
        (six.text_type('unsignedInteger'), 5, 10, 1, False),
        (six.text_type('unsignedInteger'), 5, 5, 5, True),
        (six.text_type('string'), six.text_type('hello'), 10, 4, False),
        (six.text_type('string'), six.text_type('hello'), 5, 5, True)
    )
    @ddt.unpack
    def test_serialized(self,
            valueType, currentValue, maxValue, minValue, readOnly):
        pm = PropertyModel(
            self.name, self.path, self.groupName, self.objectName,
            valueType, currentValue, maxValue, minValue, readOnly
        )
        serialized = pm.serialize()

        validate_set = [
            (pm.JSON_FIELD_NAME, self.name),
            (pm.JSON_FIELD_PATH, self.path),
            (pm.JSON_FIELD_GROUP_NAME, self.groupName),
            (pm.JSON_FIELD_OBJECT_NAME, self.objectName),
            (pm.JSON_FIELD_TYPE, valueType),
            (pm.JSON_FIELD_CURRENT_VALUE, currentValue),
            (pm.JSON_FIELD_MAXIMUM_VALUE, maxValue),
            (pm.JSON_FIELD_MINIMUM_VALUE, minValue),
            (pm.JSON_FIELD_READONLY, readOnly)
        ]

        self.assertEqual(len(serialized), len(validate_set))
        self.assertInDict(validate_set, serialized)

    @ddt.data(
        (six.text_type('float'), 5.0, 10.0, -10.0, False),
        (six.text_type('float'), 5.0, 5.0, 5.0, True),
        (six.text_type('float'), 5.0, None, 5.0, True),
        (six.text_type('float'), 5.0, 5.0, None, True),
        (six.text_type('float'), 5.0, 5.0, 5.0, None),
        (six.text_type('integer'), 5, 10, -10, False),
        (six.text_type('integer'), 5, 5, 5, True),
        (six.text_type('integer'), 5, None, 5, True),
        (six.text_type('integer'), 5, 5, None, True),
        (six.text_type('integer'), 5, 5, 5, None),
        (six.text_type('unsignedInteger'), 5, 10, 1, False),
        (six.text_type('unsignedInteger'), 5, 5, 5, True),
        (six.text_type('unsignedInteger'), 5, None, 5, True),
        (six.text_type('unsignedInteger'), 5, 5, None, True),
        (six.text_type('unsignedInteger'), 5, 5, 5, None),
        (six.text_type('string'), six.text_type('hello'), 10, 4, False),
        (six.text_type('string'), six.text_type('hello'), 5, 5, True),
        (six.text_type('string'), six.text_type('hello'), None, 5, True),
        (six.text_type('string'), six.text_type('hello'), 5, None, True),
        (six.text_type('string'), six.text_type('hello'), 5, 5, None)
    )
    @ddt.unpack
    def test_deserialized(self,
            valueType, currentValue, maxValue, minValue, readOnly):

        serialized = {
            PropertyModel.JSON_FIELD_NAME: self.name,
            PropertyModel.JSON_FIELD_PATH: self.path,
            PropertyModel.JSON_FIELD_GROUP_NAME: self.groupName,
            PropertyModel.JSON_FIELD_OBJECT_NAME: self.objectName,
            PropertyModel.JSON_FIELD_TYPE: valueType,
            PropertyModel.JSON_FIELD_CURRENT_VALUE: currentValue,
            PropertyModel.JSON_FIELD_MAXIMUM_VALUE: maxValue,
            PropertyModel.JSON_FIELD_MINIMUM_VALUE: minValue,
            PropertyModel.JSON_FIELD_READONLY: readOnly
        }

        deserialized = PropertyModel.deserialize(serialized)
        self.assertEqual(deserialized.name, self.name)
        self.assertEqual(deserialized.path, self.path)
        self.assertEqual(deserialized.groupName, self.groupName)
        self.assertEqual(deserialized.objectName, self.objectName)
        self.assertEqual(deserialized.valueType, valueType)
        self.assertEqual(deserialized.value, currentValue)

        checkMinValue = (
            minValue if minValue is not None else (
                maxValue if maxValue is not None else deserialized.MIN_VALUE
            )
        )
        checkMaxValue = (
            maxValue if maxValue is not None else deserialized.MAX_VALUE
        )
        if maxValue is None and readOnly:
            checkMaxValue = checkMinValue

        self.assertEqual(deserialized.minimum, checkMinValue)
        self.assertEqual(deserialized.maximum, checkMaxValue)

        if readOnly is not None:
            self.assertEqual(deserialized.readOnly, readOnly)
        else:
            self.assertFalse(deserialized.readOnly)

    @ddt.data(
        PropertyModel.JSON_FIELD_MAXIMUM_VALUE,
        PropertyModel.JSON_FIELD_MINIMUM_VALUE,
        PropertyModel.JSON_FIELD_READONLY
    )
    def test_deserialized_missing_field(self, field_to_remove):

        valueType = 'integer'
        currentValue = 5
        maxValue = 20
        minValue = -35
        readOnly = False

        serialized = {
            PropertyModel.JSON_FIELD_NAME: self.name,
            PropertyModel.JSON_FIELD_PATH: self.path,
            PropertyModel.JSON_FIELD_GROUP_NAME: self.groupName,
            PropertyModel.JSON_FIELD_OBJECT_NAME: self.objectName,
            PropertyModel.JSON_FIELD_TYPE: valueType,
            PropertyModel.JSON_FIELD_CURRENT_VALUE: currentValue,
            PropertyModel.JSON_FIELD_MAXIMUM_VALUE: maxValue,
            PropertyModel.JSON_FIELD_MINIMUM_VALUE: minValue,
            PropertyModel.JSON_FIELD_READONLY: readOnly
        }
        del serialized[field_to_remove]

        deserialized = PropertyModel.deserialize(serialized)
        if field_to_remove == PropertyModel.JSON_FIELD_MAXIMUM_VALUE:
            self.assertEqual(deserialized.maximum, deserialized.MAX_VALUE)
        elif field_to_remove == PropertyModel.JSON_FIELD_MINIMUM_VALUE:
            self.assertEqual(deserialized.minimum, deserialized.MIN_VALUE)
        elif field_to_remove == PropertyModel.JSON_FIELD_READONLY:
            self.assertFalse(deserialized.readOnly)
