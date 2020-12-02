from typing import Optional

from org.bobink.my_eval.eval_expression import EvalExpression, EvalValue, EvalBinOpType, EvalBinOp
from org.bobink.my_eval.lexer import Lexer, LexerIterator
from org.bobink.my_eval.tokan import TokanType, Tokan


class _ReduceResult:
    def __init__(self, op: EvalBinOpType, term: EvalExpression, right: Optional):
        self.op = op
        self.term = term
        self.right = right


class _TokanStack:
    def __init__(self, it: LexerIterator):
        self.__it = it
        self.__head = None

    def head(self):
        if self.__head is None:
            self.__head = next(self.__it)
        return self.__head

    def pop(self) -> Tokan:
        result = self.__head
        if result is None:
            return next(self.__it)
        else:
            self.__head = None
            return result


# add = mul add'
# add' = ε
# add' = "+" mul add'
# add' = "-" mul add'
#
# mul = term mul'
# mul' = ε
# mul' = "*" term mul'
# mul' = "/" term mul'
#
# term = <num>
# term = "(" add ")"

def parse(lexer: Lexer) -> EvalExpression:
    stack = _TokanStack(lexer.__iter__())
    result = _parse_add(stack)
    try:
        t = stack.head().get_type()
        print("Unexpected token: " + str(t))
        raise SyntaxError
    except StopIteration:
        return result


def _parse_add(stack: _TokanStack) -> EvalExpression:
    left = _parse_mul(stack)
    right = _parse_add_p(stack)
    while right is not None:
        left = EvalBinOp(right.op, left, right.term)
        right = right.right
    return left


def _parse_add_p(stack: _TokanStack) -> Optional[_ReduceResult]:
    try:
        head = stack.head().get_type()
        if head != TokanType.PLUS and head != TokanType.MINUS:
            return None
    except StopIteration:
        return None
    t = stack.pop().get_type()
    bin_op_t = _parse_add_op(t)
    term = _parse_mul(stack)
    expr = _parse_add_p(stack)
    return _ReduceResult(bin_op_t, term, expr)


def _parse_add_op(t: TokanType) -> EvalBinOpType:
    if t == TokanType.PLUS:
        return EvalBinOpType.PLUS
    elif t == TokanType.MINUS:
        return EvalBinOpType.MINUS
    _print_unexpected_token(TokanType.PLUS, t)
    raise SyntaxError


def _parse_mul(stack: _TokanStack) -> EvalExpression:
    left = _parse_term(stack)
    right = _parse_mul_p(stack)
    while right is not None:
        left = EvalBinOp(right.op, left, right.term)
        right = right.right
    return left


def _parse_mul_p(stack: _TokanStack) -> Optional[_ReduceResult]:
    try:
        head = stack.head().get_type()
        if head != TokanType.TIMES and head != TokanType.DIV:
            return None
    except StopIteration:
        return None
    t = stack.pop().get_type()
    bin_op_t = _parse_mul_op(t)
    term = _parse_term(stack)
    expr = _parse_mul_p(stack)
    return _ReduceResult(bin_op_t, term, expr)


def _parse_mul_op(t: TokanType) -> EvalBinOpType:
    if t == TokanType.TIMES:
        return EvalBinOpType.TIMES
    elif t == TokanType.DIV:
        return EvalBinOpType.DIV
    _print_unexpected_token(TokanType.TIMES, t)
    raise SyntaxError


def _parse_term(stack: _TokanStack) -> EvalExpression:
    n = _next_token(stack)
    t = n.get_type()
    if t == TokanType.VALUE:
        return EvalValue(n.get_value())
    if t == TokanType.LEFT_PARENTHESIS:
        expr = _parse_add(stack)
        n2 = _next_token(stack)
        if n2.get_type() != TokanType.RIGHT_PARENTHESIS:
            _print_unexpected_token(TokanType.RIGHT_PARENTHESIS, n2.get_type())
            raise SyntaxError
        return expr
    _print_unexpected_token(TokanType.VALUE, t)
    raise SyntaxError


def _next_token(stack: _TokanStack) -> Tokan:
    try:
        return stack.pop()
    except StopIteration:
        print("Unexpected end of token")
        raise SyntaxError


def _print_unexpected_token(expected: TokanType, actual: TokanType):
    print("Unexpected token. Expected: " + str(expected) + ". Got: " + str(actual))
