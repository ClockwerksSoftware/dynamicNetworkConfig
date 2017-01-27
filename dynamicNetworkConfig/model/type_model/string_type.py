import six

from dynamicNetworkConfig.model.type_model.base import BaseType
from dynamicNetworkConfig.model.type_model.errors import InvalidTypeOperation


class StringType(BaseType):

    type_name = 'string'

    def __init__(self, value, minimumLength, maximumLength, defaultValue=None):
        if defaultValue is None:
            defaultValue = ''

        super(self, StringType).__init__(
            self.type_name,
            value,
            minimumLength,
            maximumLength,
            defaultValue
        )
        assert isinstance(self.value, six.text_type)
        assert isinstance(self.default, (six.text_type, None))
        assert isinstance(self.minimum, int)
        assert isinstance(self.maximum, int)
        assert (self.minimum >= 0)
        assert (self.maximum >= self.minimum)
        if self.default is not None:
            assert (len(self.default) >= self.minimum)
            assert (len(self.default) <= self.maximum)

    def isMinimum(self, *args, **kwargs):
        return (len(self.value) == self.minimum)

    def isMaximum(self, *args, **kwargs):
        return (len(self.value) == self.maximum)

    def isDefault(self, *args, **kwargs):
        return (self.value == self.default)

    def isGreaterThan(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')

    def isGreaterThanOrEqual(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')

    def isEqual(self, other, *args, **kwargs):
        assert isinstance(other, type(self))
        return (self.value == other.value)

    def isLessThanOrEqual(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')

    def isLessThan(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')
