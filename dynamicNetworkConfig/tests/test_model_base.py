import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.base_model import BaseModel


@ddt.ddt
class TestModelBase(TestBase):

    def setUp(self):
        super(TestModelBase, self).setUp()
        self.name = 'myBaseModel'
        self.path = '/some/path/to/the/base/model'

    def tearDown(self):
        super(TestModelBase, self).tearDown()

    def test_instantiation(self):
        bm = BaseModel(self.name, self.path)
        self.assertEqual(bm.name, self.name)
        self.assertEqual(bm.path, self.path)

    @ddt.data(
        ('$ome1nv4ldN4m3$', '/path/to/invalid/name', errors.InvalidName),
        ('validName', '/inv4l1d/p4th$', errors.InvalidPath),
        ('validName', 'inv4l1d/p4th$', errors.InvalidPath),
    )
    @ddt.unpack
    def test_invalid_name(self, name, path, error):
        with self.assertRaises(error):
            BaseModel(name, path)

    def test_serialize(self):
        bm = BaseModel(self.name, self.path)

        serialized = bm.serialize()
        self.assertEqual(len(serialized), 2)
        self.assertIn(
            bm.JSON_FIELD_NAME,
            serialized
        )
        self.assertIn(
            bm.JSON_FIELD_PATH,
            serialized
        )
        self.assertEqual(serialized[bm.JSON_FIELD_NAME], self.name)
        self.assertEqual(serialized[bm.JSON_FIELD_PATH], self.path)

    def test_deserialize(self):
        serialized = {
            BaseModel.JSON_FIELD_NAME: self.name,
            BaseModel.JSON_FIELD_PATH: self.path
        }

        deserialized = BaseModel.deserialize(serialized)
        self.assertIsInstance(deserialized, BaseModel)
        self.assertEqual(deserialized.name, self.name)
        self.assertEqual(deserialized.path, self.path)

    @ddt.data(
        ('validName', True), ('1validName', True), ('validName2', True),
        ('$invalidName', False)
    )
    @ddt.unpack
    def test_validate_group_name(self, group_name, is_valid):
        if is_valid:
            BaseModel.validate_group_name(group_name)
        else:
            with self.assertRaises(errors.InvalidGroupName):
                BaseModel.validate_group_name(group_name)

    @ddt.data(
        ('validName', True), ('1validName', True), ('validName2', True),
        ('$invalidName', False)
    )
    @ddt.unpack
    def test_validate_object_name(self, object_name, is_valid):
        if is_valid:
            BaseModel.validate_object_name(object_name)
        else:
            with self.assertRaises(errors.InvalidObjectName):
                BaseModel.validate_object_name(object_name)
