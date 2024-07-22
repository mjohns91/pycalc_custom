import unittest
import calculations


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculations.add(5, 5), 10)
        self.assertEqual(calculations.add(-5, 5), 0)
        self.assertEqual(calculations.add(5.0, 5.0), 10.0)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(10, 5), 5)
        self.assertEqual(calculations.subtract(-10, 5), -15)
        self.assertEqual(calculations.subtract(-10, -5), -5)
        self.assertEqual(calculations.subtract(15.0, 5), 10.0)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(5, 5), 25)
        self.assertEqual(calculations.multiply(-5, 5), -25)
        self.assertEqual(calculations.multiply(5.0, 5), 25.0)
        self.assertEqual(calculations.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calculations.divide(25, 5), 5)
        self.assertEqual(calculations.divide(100, -10), -10)
        self.assertEqual(calculations.divide(-10, -5), 2)
        self.assertEqual(calculations.divide(10, 2.0), 5.0)
        self.assertEqual(calculations.divide(10, 3), 3.3333333333333335)
        with self.assertRaises(ZeroDivisionError):
            calculations.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
