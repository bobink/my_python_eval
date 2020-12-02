from org.bobink.my_eval.reader import Reader, ReaderIterable


class StringReaderIterable(ReaderIterable):
    def __init__(self, s: str, i: int, l: int):
        self.__s = s
        self.__i = i
        self.__l = l

    def __next__(self) -> str:
        if self.__i >= self.__l:
            raise StopIteration
        i = self.__i
        self.__i += 1
        return self.__s[i]


class StringReader(Reader):
    def __init__(self, s: str):
        self.__s = s

    def __iter__(self) -> StringReaderIterable:
        return StringReaderIterable(self.__s, 0, len(self.__s))
