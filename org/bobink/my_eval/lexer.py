from collections import Iterator, Iterable

from org.bobink.my_eval.tokan import Tokan


class LexerIterator(Iterator):
    def __next__(self) -> Tokan:
        pass


class Lexer(Iterable):
    def __iter__(self) -> LexerIterator:
        pass
