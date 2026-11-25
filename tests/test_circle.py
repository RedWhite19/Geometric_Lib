import math
import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_five(self):
        res = area(5)
        self.assertAlmostEqual(res, 25 * math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_five(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)
