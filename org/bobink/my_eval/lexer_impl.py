from org.bobink.my_eval.lexer import Lexer, LexerIterator
from org.bobink.my_eval.reader import Reader, ReaderIterable
from org.bobink.my_eval.tokan import Tokan, TokanType


class LexerIteratorImpl(LexerIterator):
    def __init__(self, reader_it: ReaderIterable):
        self.__reader_it = reader_it
        self.__last = ' '

    def __next__(self) -> Tokan:
        c = self.__last
        self.__last = ' '
        while c == ' ':
            c = next(self.__reader_it)

        if c == '+':
            return Tokan(TokanType.PLUS, 0)
        elif c == '-':
            return Tokan(TokanType.MINUS, 0)
        elif c == '*':
            return Tokan(TokanType.TIMES, 0)
        elif c == '/':
            return Tokan(TokanType.DIV, 0)
        elif c == '(':
            return Tokan(TokanType.LEFT_PARENTHESIS, 0)
        elif c == ')':
            return Tokan(TokanType.RIGHT_PARENTHESIS, 0)
        elif '0' <= c <= '9':
            value = int(c, 10) - int('0', 0)
            for c in self.__reader_it:
                if '0' <= c <= '9':
                    value = value * 10 + (int(c, 10) - int('0', 0))
                else:
                    self.__last = c
                    break
            return Tokan(TokanType.VALUE, value)
        raise ValueError


class LexerImpl(Lexer):
    def __init__(self, reader: Reader):
        self.__reader = reader

    def __iter__(self):
        return LexerIteratorImpl(iter(self.__reader))
