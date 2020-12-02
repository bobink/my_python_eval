from unittest import TestCase

from org.bobink.my_eval.my_eval import my_eval


class TestMyEval(TestCase):

    def test_eleven_plus_three(self):
        self.assertEqual(my_eval('11 + 3'), 14)

    def test_three_times_six(self):
        self.assertEqual(my_eval('3 * 6'), 18)

    def test_none(self):
        with self.assertRaises(SyntaxError):
            my_eval('')

    def test_two_three(self):
        with self.assertRaises(SyntaxError):
            my_eval('2 3')

    def test_plus(self):
        with self.assertRaises(SyntaxError):
            my_eval('+')

    def test_forty_two(self):
        self.assertEqual(my_eval('42'), 42)

    def test_two_plus_tree_times_four(self):
        self.assertEqual(my_eval('2 + 3 * 4'), 14)

    def test_two_times_tree_plus_four(self):
        self.assertEqual(my_eval('2 * 3 + 4'), 10)

    def test_p_two_plus_tree_p_times_four(self):
        self.assertEqual(my_eval('(2 + 3) * 4'), 20)

    def test_complexe(self):
        str = '5 + 9 * 89 - 23 + 65 * 4 + 42 - 23 * 2 * 3'
        self.assertEqual(my_eval(str), eval(str))
