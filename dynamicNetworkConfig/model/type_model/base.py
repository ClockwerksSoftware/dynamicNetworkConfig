"""
Base Type Model
"""


class BaseType(object):

    @classmethod
    def isInstance(cls, value):
        raise NotImplementedError

    def __init__(self, name, value, minimumValue, maximumValue, defaultValue):
        self.__name = name
        self.__value = value
        self.__minimum = minimumValue
        self.__maximum = maximumValue
        self.__default = defaultValue
        self.__is_string = False

    @property
    def is_string(self):
        return self.__is_string

    @is_string.setter
    def is_string(self, value):
        self.__is_string = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return self.__maximum

    @property
    def default(self):
        return self.__default

    def isMinimum(self, *args, **kwargs):
        raise NotImplementedError('Minimum Not Implemented')

    def isMaximum(self, *args, **kwargs):
        raise NotImplementedError('Maximum Not Implemented')

    def isDefault(self, *args, **kwargs):
        raise NotImplementedError('Default Not Implemented')

    def isGreaterThan(self, *args, **kwargs):
        raise NotImplementedError('Greater Than Not Implemented')

    def isGreaterThanOrEqual(self, *args, **kwargs):
        raise NotImplementedError('Greater Than Or Equal Not Implemented')

    def isEqual(self, *args, **kwargs):
        raise NotImplementedError('Equal Not Implemented')

    def isLessThanOrEqual(self, *args, **kwargs):
        raise NotImplementedError('Less Than Or Equal Not Implemented')

    def isLessThan(self, *args, **kwargs):
        raise NotImplementedError('Less Than Not Implemented')
