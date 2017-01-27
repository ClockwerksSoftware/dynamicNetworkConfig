from dynamicNetworkConfig.model.type_model.base import BaseType


class IntType(BaseType):

    type_name = 'integer'

    def __init__(self, value, minimum, maximum, defaultValue=None):
        if defaultValue is None:
            defaultValue = 0

        super(self, IntType).__init__(
            self.type_name,
            value,
            minimum,
            maximum,
            defaultValue
        )
        assert isinstance(self.value, int)
        assert isinstance(self.minimum, int)
        assert isinstance(self.maximum, int)
        assert isinstance(self.default, int)
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
        return (self.value == other.value)

    def isLessThanOrEqual(self, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value <= other.value)

    def isLessThan(self, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value < other.value)
