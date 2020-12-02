from collections import Iterator, Iterable


class ReaderIterable(Iterator):
    def __next__(self) -> str:
        pass


class Reader(Iterable):
    def __iter__(self) -> ReaderIterable:
        pass
