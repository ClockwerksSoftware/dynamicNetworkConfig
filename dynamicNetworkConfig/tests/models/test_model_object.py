import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.object_model import ObjectModel


@ddt.ddt
class TestModelObject(TestBase):

    def setUp(self):
        super(TestModelObject, self).setUp()
        self.name = 'myObject'
        self.groupName = 'myGroup'
        self.path = '/some/path/to/the/group'
        self.empty_properties = [
        ]

    def tearDown(self):
        super(TestModelObject, self).tearDown()

    def test_instantiation(self):
        om = ObjectModel(
            self.name, self.path, self.groupName,
            self.empty_properties
        )
        self.assertEqual(om.name, self.name)
        self.assertEqual(om.path, self.path)
        self.assertEqual(om.groupName, self.groupName)
        self.assertEqual(
            [prop for prop in om.properties],
            self.empty_properties
        )

    @ddt.data(
        ({}, errors.InvalidPropertyListing),
        ("", errors.InvalidPropertyListing),
        ('', errors.InvalidPropertyListing)
    )
    @ddt.unpack
    def test_validate_property_listing(self, property_entry, error):
        with self.assertRaises(error):
            ObjectModel(
                self.name, self.path,
                self.groupName, property_entry
            )

    def test_properties_generator(self):
        properties = [
            'one', 'two', 'three', 'four'
        ]
        om = ObjectModel(
            self.name, self.path, self.groupName,
            properties
        )
        self.assertEqual([prop for prop in om.properties], properties)

    @ddt.data(
        ("", False),
        ("howdy", True),
        (512, False)
    )
    @ddt.unpack
    def test_validate_group_name(self, name, is_valid):
        if is_valid:
            om = ObjectModel(self.name, self.path, name, self.empty_properties)
            self.assertEqual(om.groupName, name)
        else:
            with self.assertRaises(errors.InvalidGroupName):
                ObjectModel(self.name, self.path, name, self.empty_properties)

    def test_serialize(self):
        om = ObjectModel(
            self.name, self.path, self.groupName,
            self.empty_properties
        )
        serialized = om.serialize()
        self.assertEqual(len(serialized), 4)

        validate_set = [
            (om.JSON_FIELD_NAME, self.name),
            (om.JSON_FIELD_PATH, self.path),
            (om.JSON_FIELD_GROUP_NAME, self.groupName),
            (om.JSON_FIELD_SUBPROPERTIES, self.empty_properties)
        ]
        self.assertInDict(validate_set, serialized)

    def test_deserialize(self):
        serialized = {
            ObjectModel.JSON_FIELD_NAME: self.name,
            ObjectModel.JSON_FIELD_PATH: self.path,
            ObjectModel.JSON_FIELD_GROUP_NAME: self.groupName,
            ObjectModel.JSON_FIELD_SUBPROPERTIES: self.empty_properties
        }

        deserialized = ObjectModel.deserialize(serialized)
        self.assertIsInstance(deserialized, ObjectModel)
        self.assertEqual(deserialized.name, self.name)
        self.assertEqual(deserialized.path, self.path)
        self.assertEqual(deserialized.groupName, self.groupName)
        self.assertEqual(
            [prop for prop in deserialized.properties],
            self.empty_properties
        )
