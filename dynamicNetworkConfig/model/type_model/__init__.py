import six

from dynamicNetworkConfig.model.type_model.float_type import (
    FloatType,
    isclose
)
from dynamicNetworkConfig.model.type_model.int_type import IntType
from dynamicNetworkConfig.model.type_model.string_type import StringType
from dynamicNetworkConfig.model.type_model.unsigned_int_type import (
    UnsignedIntType
)


type_list = [
    FloatType,
    IntType,
    StringType,
    UnsignedIntType
]


def getType(typeName):
    typeMatching = {
        FloatType.type_name: FloatType,
        IntType.type_name: IntType,
        StringType.type_name: StringType,
        UnsignedIntType.type_name: UnsignedIntType
    }

    return typeMatching[typeName]
