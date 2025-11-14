import unittest


def area(a, b): 
    """ Принимает числа a и b, возвращает a*b что является площадью прямоугольника """
    return a * b 

def perimeter(a, b): 
    """ Принимает числа a и b, возвращает (a+b)*2 что является периметром прямоугольника """
    return (a + b)*2 

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_square_diff(self):
        res = area(56, 48)
        self.assertEqual(res, 2688)

    def test_perimeter_small(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_perimeter_diff(self):
        res = perimeter(537, 749)
        self.assertEqual(res, 2572)
        