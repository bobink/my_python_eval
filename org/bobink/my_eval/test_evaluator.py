from unittest import TestCase

from org.bobink.my_eval.eval_expression import EvalValue, EvalBinOp, EvalBinOpType
from org.bobink.my_eval.evaluator import eval_expression


class TestEvalExpressionEvaluator(TestCase):

    def test_value(self):
        v = EvalValue(66)
        self.assertEqual(eval_expression(v), 66)

    def test_plus(self):
        v = EvalBinOp(EvalBinOpType.PLUS, EvalValue(2), EvalValue(3))
        self.assertEqual(eval_expression(v), 5)

    def test_minus(self):
        v = EvalBinOp(EvalBinOpType.MINUS, EvalValue(2), EvalValue(3))
        self.assertEqual(eval_expression(v), -1)

    def test_times(self):
        v = EvalBinOp(EvalBinOpType.TIMES, EvalValue(2), EvalValue(3))
        self.assertEqual(eval_expression(v), 6)

    def test_div(self):
        v = EvalBinOp(EvalBinOpType.DIV, EvalValue(6), EvalValue(3))
        self.assertEqual(eval_expression(v), 2)