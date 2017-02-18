import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.model.json_model import JsonModel


@ddt.ddt
class TestModelJson(TestBase):

    def setUp(self):
        super(TestModelJson, self).setUp()

    def tearDown(self):
        super(TestModelJson, self).tearDown()

    def test_instantiation(self):
        jm = JsonModel([])
        self.assertIsNotNone(jm)

    @ddt.data(
        ([], True),
        (set(), False),
        (list(), True),
        ({}, False)
    )
    @ddt.unpack
    def test_validation(self, data, valid):
        jm = JsonModel(data)
        if valid:
            self.assertTrue(jm.validate())
        else:
            self.assertFalse(jm.validate())

    def test_entry(self):
        data = [0, 1, 2, 3]
        jm = JsonModel(data)

        output = [
            i
            for i in jm.entry()
        ]
        self.assertEqual(data, output)
