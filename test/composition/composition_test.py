import unittest
import numpy as np
from aavf import composition as cp


class TestComposition(unittest.TestCase):

    def test_image_size(self):
        image = np.zeros(512*512*3).reshape(512, 512, 3)
        self.assertEquals(cp.image_size(image), 512+512)