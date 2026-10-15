import math
import tempfile
import unittest
from pathlib import Path

from alpha_diversity import diversity


class DiversityTests(unittest.TestCase):
    def test_equal_abundances(self):
        result = diversity([1,1,0])
        self.assertEqual(result['richness'],2)
        self.assertAlmostEqual(result['shannon'],math.log(2))
        self.assertAlmostEqual(result['gini_simpson'],0.5)
        self.assertAlmostEqual(result['pielou'],1)

    def test_empty_and_single_feature(self):
        self.assertIsNone(diversity([0,0])['shannon'])
        self.assertIsNone(diversity([5,0])['pielou'])
        self.assertEqual(diversity([5,0])['gini_simpson'],0)

    def test_invalid_values(self):
        for value in [-1,float('nan'),float('inf')]:
            with self.assertRaises(ValueError):
                diversity([value])


if __name__ == '__main__':
    unittest.main()
