"""
"""


class DynamicNetworkConfigErrors(Exception):
    pass


class InvalidPath(DynamicNetworkConfigErrors):
    pass


class InvalidName(DynamicNetworkConfigErrors):
    pass


class InvalidGroupName(DynamicNetworkConfigErrors):
    pass


class InvalidObjectName(DynamicNetworkConfigErrors):
    pass


class InvalidGroupModel(DynamicNetworkConfigErrors):
    pass


class InvalidGroupListing(InvalidGroupModel):
    pass


class InvalidObjectListing(InvalidGroupModel):
    pass
