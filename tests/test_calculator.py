import unittest
from calculator import SafeEvaluator


class TestSafeEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = SafeEvaluator()

    def test_basic_addition(self):
        self.assertEqual(self.evaluator.evaluate("3 + 4"), 7)
        self.assertEqual(self.evaluator.evaluate("10 + 5"), 15)
        self.assertEqual(self.evaluator.evaluate("0 + 0"), 0)
        self.assertEqual(self.evaluator.evaluate("-5 + 10"), 5)

    def test_basic_subtraction(self):
        self.assertEqual(self.evaluator.evaluate("10 - 5"), 5)
        self.assertEqual(self.evaluator.evaluate("5 - 10"), -5)
        self.assertEqual(self.evaluator.evaluate("0 - 0"), 0)

    def test_basic_multiplication(self):
        self.assertEqual(self.evaluator.evaluate("3 * 4"), 12)
        self.assertEqual(self.evaluator.evaluate("10 * 0"), 0)
        self.assertEqual(self.evaluator.evaluate("-5 * 3"), -15)

    def test_basic_division(self):
        self.assertEqual(self.evaluator.evaluate("10 / 2"), 5)
        self.assertEqual(self.evaluator.evaluate("7 / 2"), 3.5)
        self.assertEqual(self.evaluator.evaluate("-10 / 2"), -5)
        self.assertEqual(self.evaluator.evaluate("10 / -2"), -5)

    def test_division_by_zero(self):
        self.assertEqual(self.evaluator.evaluate("5 / 0"), "Error")

    def test_power_operation(self):
        self.assertEqual(self.evaluator.evaluate("2 ** 3"), 8)
        self.assertEqual(self.evaluator.evaluate("9 ** 0.5"), 3.0)
        self.assertEqual(self.evaluator.evaluate("2 ** -1"), 0.5)

    def test_modulo_operation(self):
        self.assertEqual(self.evaluator.evaluate("10 % 3"), 1)
        self.assertEqual(self.evaluator.evaluate("10 % 2"), 0)
        self.assertEqual(self.evaluator.evaluate("10 % 10"), 0)

    def test_unary_operations(self):
        self.assertEqual(self.evaluator.evaluate("-5"), -5)
        self.assertEqual(self.evaluator.evaluate("-(3 + 2)"), -5)

    def test_complex_expressions(self):
        self.assertEqual(self.evaluator.evaluate("2 + 3 * 4"), 14)
        self.assertEqual(self.evaluator.evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(self.evaluator.evaluate("2 ** 3 + 5"), 13)
        self.assertEqual(self.evaluator.evaluate("10 / 2 + 3"), 8)
        self.assertEqual(self.evaluator.evaluate("10 / (2 + 3)"), 2)
        self.assertEqual(self.evaluator.evaluate("10 % 3 * 2"), 2)

    def test_invalid_expressions(self):
        self.assertEqual(self.evaluator.evaluate("2 +"), "Error")
        self.assertEqual(self.evaluator.evaluate("2 + (3"), "Error")
        self.assertEqual(self.evaluator.evaluate("2 + 3)"), "Error")
        self.assertEqual(self.evaluator.evaluate("2 & 3"), "Error")
        self.assertEqual(self.evaluator.evaluate(""), "Error")

    def test_unsupported_operations(self):
        # Testing with variables which are not supported
        self.assertEqual(self.evaluator.evaluate("x + 5"), "Error")
        # Testing with function calls which are not supported
        self.assertEqual(self.evaluator.evaluate("sin(30)"), "Error")

if __name__ == '__main__':
    unittest.main()
