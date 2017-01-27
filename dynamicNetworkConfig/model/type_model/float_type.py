from dynamicNetworkConfig.model.type_model.base import BaseType

try:
    from math import isclose
except ImportError:
    def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
        return (
            abs(a - b) <= max(
                (rel_tol * max(abs(a), abs(b))),
                abs_tol
            )
        )


class FloatType(BaseType):

    type_name = 'float'

    def __init__(self, value, minimum, maximum, defaultValue):
        if defaultValue is None:
            defaultValue = 0.0

        super(self, FloatType).__init__(
            self.type_name,
            value,
            minimum,
            maximum,
            defaultValue
        )
        assert isinstance(self.value, float)
        assert isinstance(self.minimum, float)
        assert isinstance(self.maximum, float)
        assert isinstance(self.default, float)
        assert (self.maximum >= self.minimum)

    def isMinimum(self, *args, **kwargs):
        return (len(self.value) == self.minimum)

    def isMaximum(self, *args, **kwargs):
        return (len(self.value) == self.maximum)

    def isDefault(self, *args, **kwargs):
        return (self.value == self.default)

    def isGreaterThan(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value > other.value)

    def isGreaterThanOrEqual(self, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value >= other.value)

    def isEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return isclose(
            self.value,
            other.value,
            rel_tol=relative_tolerance,
            abs_tol=absolute_tolerance
        )

    def isLessThanOrEqual(self, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value <= other.value)

    def isLessThan(self, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value < other.value)
