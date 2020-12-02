from org.bobink.my_eval.evaluator import eval_expression
from org.bobink.my_eval.lexer_impl import LexerImpl

from org.bobink.my_eval.parser import parse
from org.bobink.my_eval.string_reader import StringReader


def my_eval(s: str) -> int:
    expr = parse(LexerImpl(StringReader(s)))
    return eval_expression(expr)
