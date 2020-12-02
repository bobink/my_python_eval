from enum import Enum


class EvalExpressionVisitor:
    def visit_bin_op(self, e):
        pass

    def visit_value(self, e):
        pass


class EvalExpression:
    def accept(self, v: EvalExpressionVisitor):
        pass


class EvalBinOpType(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4


class EvalBinOp(EvalExpression):
    def __init__(self, op: EvalBinOpType, left: EvalExpression, right: EvalExpression):
        self.__op = op
        self.__left = left
        self.__right = right

    def accept(self, v: EvalExpressionVisitor):
        v.visit_bin_op(self)

    def get_type(self):
        return self.__op

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right


class EvalValue(EvalExpression):
    def __init__(self, v: int):
        self.__value = v

    def accept(self, v: EvalExpressionVisitor):
        v.visit_value(self)

    def get_value(self):
        return self.__value

