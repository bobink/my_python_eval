from enum import Enum


class TokanType(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    LEFT_PARENTHESIS = 5
    RIGHT_PARENTHESIS = 6
    VALUE = 7


class Tokan:
    def __init__(self, __type: TokanType, __value: int):
        self.__type = __type
        self.__value = __value

    def get_type(self) -> TokanType:
        return self.__type

    def get_value(self) -> int:
        return self.__value

    def __eq__(self, other):
        if not isinstance(other, Tokan):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__type == other.__type and self.__value == other.__value

    def __repr__(self):
        return str(self.__type) + ' ' + str(self.__value)
