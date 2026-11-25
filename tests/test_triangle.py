import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(4, 5)
        self.assertEqual(res, 10.0)

    def test_area_odd(self):
        res = area(3, 4)
        self.assertEqual(res, 6.0)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_int(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = perimeter(1.5, 2.5, 3)
        self.assertEqual(res, 7.0)
