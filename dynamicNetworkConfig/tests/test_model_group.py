import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.group_model import GroupModel


@ddt.ddt
class TestModelGroup(TestBase):

    def setUp(self):
        super(TestModelGroup, self).setUp()
        self.name = 'myGroup'
        self.path = '/some/path/to/the/group'
        self.empty_groups = [
        ]
        self.empty_objects = [
        ]


    def tearDown(self):
        super(TestModelGroup, self).tearDown()

    def test_instantiation(self):
        gm = GroupModel(
            self.name, self.path,
            self.empty_groups, self.empty_objects
        )
        self.assertEqual(gm.name, self.name)
        self.assertEqual(gm.path, self.path)
        self.assertEqual([group for group in gm.groups], self.empty_groups)
        self.assertEqual([obj for obj in gm.objects], self.empty_objects)

    @ddt.data(
        ({}, errors.InvalidGroupListing),
        ("", errors.InvalidGroupListing),
        ('', errors.InvalidGroupListing)
    )
    @ddt.unpack
    def test_validate_group_listing(self, group_entry, error):
        with self.assertRaises(error):
            GroupModel(self.name, self.path, group_entry, self.empty_objects)

    @ddt.data(
        ({}, errors.InvalidObjectListing),
        ("", errors.InvalidObjectListing),
        ('', errors.InvalidObjectListing)
    )
    @ddt.unpack
    def test_validate_object_listing(self, object_entry, error):
        with self.assertRaises(error):
            GroupModel(self.name, self.path, self.empty_groups, object_entry)

    def test_group_generator(self):
        groups = [
            'one', 'two', 'three', 'four'
        ]
        gm = GroupModel(
            self.name, self.path,
            groups, self.empty_objects
        )
        self.assertEqual([group for group in gm.groups], groups)

    def test_object_generator(self):
        objects = [
            'one', 'two', 'three', 'four'
        ]
        gm = GroupModel(
            self.name, self.path,
            self.empty_groups, objects
        )
        self.assertEqual([obj for obj in gm.objects], objects)

    @ddt.data(
        ('/', True),
        ('/some/other/path', False)
    )
    @ddt.unpack
    def test_is_root(self, path, is_root):
        gm = GroupModel(
            self.name, path,
            self.empty_groups, self.empty_objects
        )
        self.assertEqual(gm.path, path)
        self.assertEqual(gm.is_root, is_root)

    def test_serialize(self):
        gm = GroupModel(
            self.name, self.path,
            self.empty_groups, self.empty_objects
        )
        serialized = gm.serialize()
        self.assertEqual(len(serialized), 4)

        validate_set = [
            (gm.JSON_FIELD_NAME, self.name),
            (gm.JSON_FIELD_PATH, self.path),
            (gm.JSON_FIELD_SUBGROUPS, self.empty_groups),
            (gm.JSON_FIELD_SUBOBJECTS, self.empty_objects)
        ]
        self.assertInDict(validate_set, serialized)

    def test_deserialize(self):
        serialized = {
            GroupModel.JSON_FIELD_NAME: self.name,
            GroupModel.JSON_FIELD_PATH: self.path,
            GroupModel.JSON_FIELD_SUBGROUPS: self.empty_groups,
            GroupModel.JSON_FIELD_SUBOBJECTS: self.empty_objects
        }

        deserialized = GroupModel.deserialize(serialized)
        self.assertIsInstance(deserialized, GroupModel)
        self.assertEqual(deserialized.name, self.name)
        self.assertEqual(deserialized.path, self.path)
        self.assertEqual(
            [group for group in deserialized.groups],
            self.empty_groups
        )
        self.assertEqual(
            [obj for obj in deserialized.objects],
            self.empty_objects
        )
