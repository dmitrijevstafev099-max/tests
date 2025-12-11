import math
import unittest
# Импортирую модуль math для получения math.pi

def area(r):
    return math.pi * r * r #Функция для вычисления площади круга


def perimeter(r):
    return 2 * math.pi * r#Функция для вычисления периметра окружности
pi = math.pi
class CircleleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(11)
        self.assertEqual(res, 11*11*pi)
    
    def test_perimeter_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(10)
        self.assertEqual(res, 2*10*pi)
    