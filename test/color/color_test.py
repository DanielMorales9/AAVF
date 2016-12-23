import os
import unittest
import numpy as np
from aavf import color


class TestColor(unittest.TestCase):

    def test_basic_color_amount(self):
        image = np.zeros(512 * 512 * 3).reshape(512, 512, 3)
        label_path = os.path.join(os.path.dirname(__file__), "..", "..", "file", "maxcolor.csv")
        labels = np.genfromtxt(label_path, dtype=int)
        expected = np.zeros(11, dtype=float)
        expected[0] = 100
        eq = color.basic_color_amount(image, labels) == expected
        self.assertTrue(np.all(eq))

    def test_hsv_statistics(self):
        image = np.zeros(512 * 512 * 3).reshape(512, 512, 3)
        self.assertEquals(color.hsv_statistics(image), (0., 0., 0., 0., 0.))

    def test_pleasure_arousal_dominance(self):
        self.assertEquals(color.pleasure_arousal_dominance(0, 0), (0, 0, 0))
