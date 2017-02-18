import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.model.type_model import errors
from dynamicNetworkConfig.model.type_model.string_type import StringType


@ddt.ddt
class TestModelTypeBase(TestBase):

    def setUp(self):
        super(TestModelTypeBase, self).setUp()
        self.name = "string"
        self.value = "show"
        self.min = 4
        self.max = 4

    def tearDown(self):
        super(TestModelTypeBase, self).tearDown()

    def test_instantiation(self):
        st = StringType(
            self.value,
            self.min,
            self.max
        )

        self.assertEqual(self.name, st.name)
        self.assertEqual(self.value, st.value)
        self.assertEqual(self.min, st.minimum)
        self.assertEqual(self.max, st.maximum)
        self.assertTrue(st.isEqual(self.value))
        self.assertEqual('', st.default)
        self.assertFalse(st.isDefault())

        with self.assertRaises(errors.InvalidTypeOperation):
            st.isGreaterThan('little bo peep has lost her sheep')

        with self.assertRaises(errors.InvalidTypeOperation):
            st.isGreaterThanOrEqual('and does not know where to find them')

        with self.assertRaises(errors.InvalidTypeOperation):
            st.isLessThanOrEqual('leave them alone, and they will come home')

        with self.assertRaises(errors.InvalidTypeOperation):
            st.isLessThan('wagging their tails behind them')

    @ddt.data(
        ("hello", "world", False),
        ("oxygen", "oxygen", True)
    )
    @ddt.unpack
    def test_equal(self, value, other, is_equal):
        st1 = StringType(
            value,
            0,
            2 * len(value)
        )
        st2 = StringType(
            other,
            0,
            2 * len(other)
        )
        self.assertEqual(st1.isEqual(st2), is_equal)
        self.assertEqual(st1.isEqual(other), is_equal)

    @ddt.data(
        -1, 0, 1, 5.0, 1e5
    )
    def test_equal_invalid_operation(self, value):
        st = StringType(
            self.value,
            self.min,
            self.max
        )
        with self.assertRaises(errors.InvalidTypeOperation):
            st.isEqual(value)

    @ddt.data(
        ("hello", 5, True),
        ("hello", 4, False)
    )
    @ddt.unpack
    def test_minimum(self, value, minimum, is_minimum):
        st = StringType(
            value,
            minimum,
            minimum + 5
        )
        self.assertEqual(is_minimum, st.isMinimum())

    @ddt.data(
        ("hello", 5, True),
        ("hello", 10, False)
    )
    @ddt.unpack
    def test_maximum(self, value, maximum, is_maximum):
        st = StringType(
            value,
            0,
            maximum
        )
        self.assertEqual(is_maximum, st.isMaximum())
