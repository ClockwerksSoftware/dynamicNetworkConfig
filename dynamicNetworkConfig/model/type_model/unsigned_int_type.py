from dynamicNetworkConfig.model.type_model.int_type import IntType


class UnsignedIntType(IntType):

    type_name = 'unsignedInteger'

    def __init__(self, maximum, defaultValue):
        if defaultValue is None:
            defaultValue = 0

        super(self, IntType).__init__(self.type_name, 0, maximum, defaultValue)
        assert (self.minimum >= 0)
