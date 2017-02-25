import six

from dynamicNetworkConfig.model.type_model.base import BaseType

try:
    from math import isclose

except ImportError:  # noqa
    def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
        return (
            abs(a - b) <= max(
                (rel_tol * max(abs(a), abs(b))),
                abs_tol
            )
        )


class FloatType(BaseType):

    type_name = six.text_type('float')
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')
    DEFAULT_VALUE = 0.0
    DEFAULT_RELATIVE_TOLERANCE = 0.0000001
    DEFAULT_ABSOLUTE_TOLERANCE = 0.0000001

    @classmethod
    def isInstance(cls, value):
        return isinstance(value, float)

    def __init__(self, value, minimum, maximum, defaultValue=None,
                 readOnly=False):
        if defaultValue is None:
            defaultValue = self.DEFAULT_VALUE

        if minimum is None:
            if readOnly is True:
                minimum = maximum if maximum is not None else minimum
            else:
                minimum = self.MIN_VALUE

        if maximum is None:
            if readOnly is True:
                maximum = minimum
            else:
                maximum = self.MAX_VALUE

        super(FloatType, self).__init__(
            self.type_name,
            value,
            minimum,
            maximum,
            defaultValue
        )
        assert self.isInstance(self.value)
        assert self.isInstance(self.minimum)
        assert self.isInstance(self.maximum)
        assert self.isInstance(self.default)
        assert (self.maximum >= self.minimum)

    def isMinimum(self, *args, **kwargs):
        return (self.value == self.minimum)

    def isMaximum(self, *args, **kwargs):
        return (self.value == self.maximum)

    def isDefault(self, *args, **kwargs):
        return (self.value == self.default)

    def isGreaterThan(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value > other.value)

    def isGreaterThanOrEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value >= other.value)

    def isEqual(self, other,
                relative_tolerance=None,
                absolute_tolerance=None,
                *args, **kwargs):
        assert isinstance(other, type(self))

        if relative_tolerance is None:
            relative_tolerance = self.DEFAULT_RELATIVE_TOLERANCE

        if absolute_tolerance is None:
            absolute_tolerance = self.DEFAULT_ABSOLUTE_TOLERANCE

        return isclose(
            self.value,
            other.value,
            rel_tol=relative_tolerance,
            abs_tol=absolute_tolerance
        )

    def isLessThanOrEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value <= other.value)

    def isLessThan(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value < other.value)
