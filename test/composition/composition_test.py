import unittest
import numpy as np
from aavf import composition as cp


class TestComposition(unittest.TestCase):

    def test_image_size(self):
        image = np.zeros(512*512*3).reshape(512, 512, 3)
        self.assertEquals(cp.image_size(image), 512+512)

    def test_rule_of_third(self):
        image = np.ones(512*512*3).reshape(512, 512, 3)
        self.assertEqual(cp.rule_of_third(image), (0.9922027587890625, 0.9922027587890625))
