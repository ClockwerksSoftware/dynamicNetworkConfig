import six

from dynamicNetworkConfig.model.type_model.base import BaseType
from dynamicNetworkConfig.model.type_model.errors import InvalidTypeOperation


class StringType(BaseType):

    type_name = six.text_type('string')
    MIN_VALUE = 0
    # for the purposes here, and especially since this can be overriden
    # the maximum of 32k should be sufficient
    MAX_VALUE = 32768

    @classmethod
    def isInstance(cls, value):
        return isinstance(value, six.string_types)

    def __init__(self, value, minimumLength, maximumLength, defaultValue=None,
                 readOnly=False):
        customDefaultValue = True
        if defaultValue is None:
            defaultValue = ''
            customDefaultValue = False

        if minimumLength is None:
            minimumLength = self.MIN_VALUE

        if maximumLength is None:
            if readOnly:
                maximumLength = minimumLength
            else:
                maximumLength = self.MAX_VALUE

        super(StringType, self).__init__(
            self.type_name,
            value,
            minimumLength,
            maximumLength,
            defaultValue
        )
        self.is_string = True
        assert isinstance(self.value, six.string_types)
        assert isinstance(self.default, (six.string_types, None))
        assert isinstance(self.minimum, int)
        assert isinstance(self.maximum, int)
        assert (self.minimum >= 0)
        assert (self.maximum >= self.minimum)
        if customDefaultValue:
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
        if isinstance(other, type(self)):
            return (self.value == other.value)

        elif self.isInstance(other):
            return (self.value == other)

        else:
            raise InvalidTypeOperation('Cannot convert types')

    def isLessThanOrEqual(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')

    def isLessThan(self, *args, **kwargs):
        raise InvalidTypeOperation('Invalid Comparison for Strings')
