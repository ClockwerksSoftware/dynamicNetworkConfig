import sys

import six

from dynamicNetworkConfig.model.type_model.base import BaseType


class IntType(BaseType):

    type_name = six.text_type('integer')
    MIN_VALUE = ((sys.maxsize * -1) - 1)
    MAX_VALUE = sys.maxsize
    DEFAULT_VALUE = 0

    @classmethod
    def isInstance(cls, value):
        return isinstance(value, int)

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

        super(IntType, self).__init__(
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

    def isEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value == other.value)

    def isLessThanOrEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value <= other.value)

    def isLessThan(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value < other.value)
