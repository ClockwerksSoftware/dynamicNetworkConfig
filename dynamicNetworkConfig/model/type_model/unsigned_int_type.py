import six

from dynamicNetworkConfig.model.type_model.int_type import IntType


class UnsignedIntType(IntType):

    type_name = six.text_type('unsignedInteger')
    MIN_VALUE = 0

    def __init__(self, value, minimum, maximum, defaultValue=None,
                 readOnly=False):
        if defaultValue is None:
            defaultValue = 0

        if minimum is None:
            minimum = self.MIN_VALUE

        super(UnsignedIntType, self).__init__(
            value,
            max(0, minimum),
            maximum,
            defaultValue=defaultValue,
            readOnly=readOnly
        )
        self._BaseType__name = self.type_name
        assert (self.minimum >= 0)
