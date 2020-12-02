from unittest import TestCase

from org.bobink.my_eval.string_reader import StringReader


class TestStringReader(TestCase):

    def test_simple_string(self):
        reader = StringReader('bobink')
        it = iter(reader)
        self.assertEqual(next(it), 'b')
        self.assertEqual(next(it), 'o')
        self.assertEqual(next(it), 'b')
        self.assertEqual(next(it), 'i')
        self.assertEqual(next(it), 'n')
        self.assertEqual(next(it), 'k')
        with self.assertRaises(StopIteration):
            next(it)