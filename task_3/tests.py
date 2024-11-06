import unittest

from util import calculate_difference


class CalculateDifferenceTest(unittest.TestCase):
    def test_0_minus_0(self):
        h1 = 0
        h2 = 0
        diff = calculate_difference(h1, h2)
        self.assertEqual(0, diff)

    def test_12_minus_12(self):
        h1 = 12
        h2 = 12
        diff = calculate_difference(h1, h2)
        self.assertEqual(0, diff)

    def test_1_minus_23(self):
        h1 = 1
        h2 = 23
        diff = calculate_difference(h1, h2)
        self.assertEqual(2, diff)

    def test_0_minus_4(self):
        h1 = 0
        h2 = 4
        diff = calculate_difference(h1, h2)
        self.assertEqual(20, diff)

    def test_4_minus_0(self):
        h1 = 4
        h2 = 0
        diff = calculate_difference(h1, h2)
        self.assertEqual(4, diff)

    def test_all_cases(self):
        for h1 in range(0, 23):
            for h2 in range(0, 23):
                expected_diff = (h1 - h2) % 24
                actual_diff = calculate_difference(h1, h2)

                self.assertEqual(expected_diff, actual_diff)

    def test_invalid_inputs(self):
        test_cases = [(-1, 0), (0, -1), (24, 0), (0, 24)]
        for h1, h2 in test_cases:
            with self.assertRaises(Exception):
                calculate_difference(h1, h2)



