import unittest


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


class MyTestCase(unittest.TestCase):
    def test_2つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))  # add assertion here
        self.assertEqual(12, add(8, 4))  # add assertion here

    def test_2つの整数の差を計算できる(self):
        self.assertEqual(1, sub(4, 3))
        self.assertEqual(5, sub(12, 7))

    def test_2つの整数の積を計算できる(self):
        self.assertEqual(15, mul(3, 5))
        self.assertEqual(24, mul(3, 8))

    def test_2つの整数の除を計算できる(self):
        self.assertEqual(4, div(12, 3))
        self.assertEqual(9, div(81, 9))


if __name__ == '__main__':
    unittest.main()
