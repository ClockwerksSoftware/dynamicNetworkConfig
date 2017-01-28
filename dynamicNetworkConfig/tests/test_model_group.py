import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.model.group_model import GroupModel


@ddt.ddt
class TestModelGroup(TestBase):

    def setUp(self):
        super(TestModelGroup, self).setUp()
        self.name = 'myGroup'
        self.path = '/some/path/to/the/group'

    def tearDown(self):
        super(TestModelGroup, self).tearDown()

    def test_instantiation(self):
        groups = [
        ]
        objects = [
        ]

        gm = GroupModel(self.name, self.path, groups, objects)
        self.assertEqual([group for group in gm.groups], groups)
        self.assertEqual([obj for obj in gm.objects], objects)
