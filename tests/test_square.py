import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_float(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_int(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_float(self):
        res = perimeter(0.25)
        self.assertEqual(res, 1.0)
