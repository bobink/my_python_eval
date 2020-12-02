from org.bobink.my_eval.eval_expression import EvalExpressionVisitor, EvalBinOp, EvalValue, EvalExpression, EvalBinOpType


class _EvalExpressionEvaluator(EvalExpressionVisitor):
    def __init__(self):
        self.result = 0

    def visit_bin_op(self, e: EvalBinOp):
        op = e.get_type()
        left = eval_expression(e.get_left())
        right = eval_expression(e.get_right())
        self.result = self.eval_bin_op(op, left, right)

    @staticmethod
    def eval_bin_op(op: EvalBinOpType, left: int, right: int) -> int:
        if op == EvalBinOpType.PLUS:
            return left + right
        elif op == EvalBinOpType.MINUS:
            return left - right
        elif op == EvalBinOpType.TIMES:
            return left * right
        elif op == EvalBinOpType.DIV:
            return int(left / right)
        else:
            raise ValueError

    def visit_value(self, e: EvalValue):
        self.result = e.get_value()

    def get_result(self):
        return self.result


def eval_expression(e: EvalExpression) -> int:
    visitor = _EvalExpressionEvaluator()
    e.accept(visitor)
    return visitor.get_result()
