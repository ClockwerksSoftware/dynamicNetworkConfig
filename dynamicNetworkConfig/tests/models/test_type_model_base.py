import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.type_model.base import BaseType


@ddt.ddt
class TestModelTypeBase(TestBase):

    def setUp(self):
        super(TestModelTypeBase, self).setUp()
        self.name = "baseType"
        self.value = "show"
        self.min = "howdy"
        self.max = "doody"
        self.default = 1950

    def tearDown(self):
        super(TestModelTypeBase, self).tearDown()

    def test_instantiation(self):
        tb = BaseType(
            self.name,
            self.value,
            self.min,
            self.max,
            self.default
        )

        self.assertEqual(self.name, tb.name)
        self.assertEqual(self.value, tb.value)
        self.assertEqual(self.min, tb.minimum)
        self.assertEqual(self.max, tb.maximum)
        self.assertEqual(self.default, tb.default)

        with self.assertRaises(NotImplementedError):
            tb.isInstance("baaa")

        with self.assertRaises(NotImplementedError):
            tb.isMinimum("black")

        with self.assertRaises(NotImplementedError):
            tb.isMaximum("sheep")

        with self.assertRaises(NotImplementedError):
            tb.isDefault("have")

        with self.assertRaises(NotImplementedError):
            tb.isGreaterThan("you")

        with self.assertRaises(NotImplementedError):
            tb.isGreaterThanOrEqual("any")

        with self.assertRaises(NotImplementedError):
            tb.isEqual("wool")

        with self.assertRaises(NotImplementedError):
            tb.isLessThanOrEqual("yes sir, yes sir")

        with self.assertRaises(NotImplementedError):
            tb.isLessThan("3 bags full")
