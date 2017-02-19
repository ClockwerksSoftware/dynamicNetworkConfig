import six

from dynamicNetworkConfig.model.type_model.int_type import IntType


class UnsignedIntType(IntType):

    type_name = six.text_type('unsignedInteger')
    MIN_VALUE = 0
    DEFAULT_VALUE = 0

    def __init__(self, value, minimum, maximum, defaultValue=None,
                 readOnly=False):
        if defaultValue is None:
            defaultValue = self.DEFAULT_VALUE

        if minimum is None:
            if readOnly is True:
                minimum = maximum if maximum is not None else minimum
            else:
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
