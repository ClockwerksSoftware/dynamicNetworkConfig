import ddt

from dynamicNetworkConfig.tests import TestBase

from dynamicNetworkConfig.common import errors
from dynamicNetworkConfig.model.type_model.float_type import FloatType


@ddt.ddt
class TestModelTypeModelFloat(TestBase):

    def setUp(self):
        super(TestModelTypeModelFloat, self).setUp()

    def tearDown(self):
        super(TestModelTypeModelFloat, self).tearDown()

    @ddt.data(
        (1, False), (1.0, True), ('hello', False)
    )
    @ddt.unpack
    def test_is_instance(self, value, matches):
        self.assertEqual(
            matches,
            FloatType.isInstance(value)
        )

    @ddt.data(
        (5.0, -10.0, 10.0, 0.0, False),
        (5.0, 5.0, 5.0, 5.0, True),
        (5.0, 5.0, 5.0, 5.0, False),
        (5.0, None, 5.0, 5.0, False),
        (5.0, None, 5.0, 5.0, True),
        (5.0, 5.0, None, 5.0, False),
        (5.0, 5.0, None, 5.0, True),
        (5.0, None, None, 5.0, False),
        (5.0, 5.0, 5.0, None, False),
        (5.0, 5.0, 5.0, 5.0, None),
    )
    @ddt.unpack
    def test_instantiation(self, value, minimum, maximum, default, readOnly):
        it = FloatType(
            value, minimum, maximum,
            defaultValue=default,
            readOnly=readOnly
        )

        checkMinValue = (
            minimum if minimum is not None else (
                maximum if readOnly else FloatType.MIN_VALUE
            )
        )
        checkMaxValue = (
            maximum if maximum is not None else FloatType.MAX_VALUE
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
        (FloatType.MIN_VALUE, None, True),
        (5.0, None, False),
        (5.0, 10.0, False),
        (5.0, 5.0, True)
    )
    @ddt.unpack
    def test_is_minimum(self, value, minimum, is_minimum):
        it = FloatType(
            value,
            minimum,
            None
        )

        checkMinValue = (
            minimum if minimum is not None else FloatType.MIN_VALUE
        )
        self.assertEqual(it.minimum, checkMinValue)
        self.assertEqual(it.isMinimum(), is_minimum)

    @ddt.data(
        (FloatType.MAX_VALUE, None, True),
        (5.0, None, False),
        (5.0, 10.0, False),
        (5.0, 5.0, True)
    )
    @ddt.unpack
    def test_is_maximum(self, value, maximum, is_maximum):
        it = FloatType(
            value,
            None,
            maximum
        )

        checkMaxValue = (
            maximum if maximum is not None else FloatType.MAX_VALUE
        )
        self.assertEqual(it.maximum, checkMaxValue)
        self.assertEqual(it.isMaximum(), is_maximum)

    @ddt.data(
        (FloatType.DEFAULT_VALUE, None, True),
        (5.0, None, False),
        (5.0, 10.0, False),
        (5.0, 5.0, True)
    )
    @ddt.unpack
    def test_is_default(self, value, default, is_default):
        it = FloatType(
            value,
            None,
            None,
            default
        )

        checkValue = (
            default if default is not None else FloatType.DEFAULT_VALUE
        )
        self.assertEqual(it.default, checkValue)
        self.assertEqual(it.isDefault(), is_default)

    @ddt.data(
        (5.0, 10.0, True, True, False, False, False),
        (10.0, 10.0, False, True, True, True, False),
        (10.0, 5.0, False, False, False, True, True)
    )
    @ddt.unpack
    def test_comparison(self, value1, value2, lt, lte, eq, gte, gt):
        it1 = FloatType(value1, None, None)
        it2 = FloatType(value2, None, None)

        self.assertEqual(it1.isLessThan(it2), lt)
        self.assertEqual(it1.isLessThanOrEqual(it2), lte)
        self.assertEqual(it1.isEqual(it2), eq)
        self.assertEqual(it1.isGreaterThanOrEqual(it2), gte)
        self.assertEqual(it1.isGreaterThan(it2), gt)

    @ddt.data(
        (None, None, False),
        (0.1, None, True),
        (None, 0.1, True),
        (0.1, 0.1, True)
    )
    @ddt.unpack
    def test_is_equal(self, absolute_tolerance, relative_tolerance, is_equal):
        it1 = FloatType(5.5, None, None)
        it2 = FloatType(5.51, None, None)

        self.assertEqual(
            it1.isEqual(
                it2,
                absolute_tolerance=absolute_tolerance,
                relative_tolerance=relative_tolerance
            ),
            is_equal
        )
