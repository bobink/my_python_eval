from unittest import TestCase

from org.bobink.my_eval.lexer import Lexer, LexerIterator
from org.bobink.my_eval.lexer_impl import LexerImpl
from org.bobink.my_eval.string_reader import StringReader
from org.bobink.my_eval.tokan import Tokan, TokanType


class TestLexerString(TestCase):

    def test_eleven_plus_three(self):
        ls = iter(LexerImpl(StringReader("11 + 3")))
        self.assert_next_token_is_value(ls, 11)
        self.assert_next_token_type(ls, TokanType.PLUS)
        self.assert_next_token_is_value(ls, 3)
        self.assert_no_more_token(ls)

    def test_big_whitespace(self):
        ls = iter(LexerImpl(StringReader("   325      +123*    66")))
        self.assert_next_token_is_value(ls, 325)
        self.assert_next_token_type(ls, TokanType.PLUS)
        self.assert_next_token_is_value(ls, 123)
        self.assert_next_token_type(ls, TokanType.TIMES)
        self.assert_next_token_is_value(ls, 66)
        self.assert_no_more_token(ls)

    def assert_next_token(self, ls: LexerIterator, t: Tokan):
        self.assertEqual(next(ls), t)

    def assert_next_token_is_value(self, ls: LexerIterator, v: int):
        self.assert_next_token(ls, Tokan(TokanType.VALUE, v))

    def assert_next_token_type(self, ls: LexerIterator, t: TokanType):
        self.assert_next_token(ls, Tokan(t, 0))

    def assert_no_more_token(self, ls: LexerIterator):
        with self.assertRaises(StopIteration):
            next(ls)
