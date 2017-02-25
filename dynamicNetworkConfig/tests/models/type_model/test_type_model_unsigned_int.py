import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.type_model.unsigned_int_type import (
    UnsignedIntType
)


@ddt.ddt
class TestModelTypeModelUnsignedInt(TestBase):

    def setUp(self):
        super(TestModelTypeModelUnsignedInt, self).setUp()

    def tearDown(self):
        super(TestModelTypeModelUnsignedInt, self).tearDown()

    @ddt.data(
        (1, True), (1.0, False), ('hello', False)
    )
    @ddt.unpack
    def test_is_instance(self, value, matches):
        self.assertEqual(
            matches,
            UnsignedIntType.isInstance(value)
        )

    @ddt.data(
        (5, 0, 10, 0, False),
        (5, 5, 5, 5, True),
        (5, 5, 5, 5, False),
        (5, None, 5, 5, False),
        (5, None, 5, 5, True),
        (5, 5, None, 5, False),
        (5, 5, None, 5, True),
        (5, None, None, 5, False),
        (5, 5, 5, None, False),
        (5, 5, 5, 5, None),
    )
    @ddt.unpack
    def test_instantiation(self, value, minimum, maximum, default, readOnly):
        it = UnsignedIntType(
            value, minimum, maximum,
            defaultValue=default,
            readOnly=readOnly
        )

        checkMinValue = (
            minimum if minimum is not None else (
                maximum if readOnly else UnsignedIntType.MIN_VALUE
            )
        )
        checkMaxValue = (
            maximum if maximum is not None else UnsignedIntType.MAX_VALUE
        )
        if maximum is None and readOnly:
            checkMaxValue = checkMinValue

        self.assertEqual(it.value, value)
        self.assertEqual(it.minimum, checkMinValue)
        self.assertEqual(it.maximum, checkMaxValue)
        if default is not None:
            self.assertEqual(it.default, default)
        else:
            self.assertEqual(it.default, it.DEFAULT_VALUE)

    @ddt.data(
        (5, -10, 10, 0, False),
    )
    @ddt.unpack
    def test_instantiation_no_negatives(self, value, minimum, maximum,
                                        default, readOnly):
        it = UnsignedIntType(
            value, minimum, maximum,
            defaultValue=default,
            readOnly=readOnly
        )
        checkMinValue = (
            minimum if (
                minimum is not None and minimum >= UnsignedIntType.MIN_VALUE
            ) else (
                maximum if readOnly else UnsignedIntType.MIN_VALUE
            )
        )
        checkMaxValue = (
            maximum if maximum is not None else UnsignedIntType.MAX_VALUE
        )
        if maximum is None and readOnly:
            checkMaxValue = checkMinValue

        self.assertEqual(it.value, value)
        self.assertEqual(it.minimum, checkMinValue)
        self.assertEqual(it.maximum, checkMaxValue)
        if default is not None:
            self.assertEqual(it.default, default)
        else:
            self.assertEqual(it.default, it.DEFAULT_VALUE)

    @ddt.data(
        (UnsignedIntType.MIN_VALUE, None, True),
        (5, None, False),
        (5, 10, False),
        (5, 5, True)
    )
    @ddt.unpack
    def test_is_minimum(self, value, minimum, is_minimum):
        it = UnsignedIntType(
            value,
            minimum,
            None
        )

        checkMinValue = (
            minimum if minimum is not None else UnsignedIntType.MIN_VALUE
        )
        self.assertEqual(it.minimum, checkMinValue)
        self.assertEqual(it.isMinimum(), is_minimum)

    @ddt.data(
        (UnsignedIntType.MAX_VALUE, None, True),
        (5, None, False),
        (5, 10, False),
        (5, 5, True)
    )
    @ddt.unpack
    def test_is_maximum(self, value, maximum, is_maximum):
        it = UnsignedIntType(
            value,
            None,
            maximum
        )

        checkMaxValue = (
            maximum if maximum is not None else UnsignedIntType.MAX_VALUE
        )
        self.assertEqual(it.maximum, checkMaxValue)
        self.assertEqual(it.isMaximum(), is_maximum)

    @ddt.data(
        (UnsignedIntType.DEFAULT_VALUE, None, True),
        (5, None, False),
        (5, 10, False),
        (5, 5, True)
    )
    @ddt.unpack
    def test_is_default(self, value, default, is_default):
        it = UnsignedIntType(
            value,
            None,
            None,
            default
        )

        checkValue = (
            default if default is not None else UnsignedIntType.DEFAULT_VALUE
        )
        self.assertEqual(it.default, checkValue)
        self.assertEqual(it.isDefault(), is_default)

    @ddt.data(
        (5, 10, True, True, False, False, False),
        (10, 10, False, True, True, True, False),
        (10, 5, False, False, False, True, True)
    )
    @ddt.unpack
    def test_comparison(self, value1, value2, lt, lte, eq, gte, gt):
        it1 = UnsignedIntType(value1, None, None)
        it2 = UnsignedIntType(value2, None, None)

        self.assertEqual(it1.isLessThan(it2), lt)
        self.assertEqual(it1.isLessThanOrEqual(it2), lte)
        self.assertEqual(it1.isEqual(it2), eq)
        self.assertEqual(it1.isGreaterThanOrEqual(it2), gte)
        self.assertEqual(it1.isGreaterThan(it2), gt)
