import unittest


def area(a):
    """ Принимает число a, возвращает a*a что является площадью квадрата """
    return a * a


def perimeter(a):
    """ Принимает число a, возвращает a*4 что является периметром квадрата """
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    
    def test_perimeter_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(10)
        self.assertEqual(res, 40)