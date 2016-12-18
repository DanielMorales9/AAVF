import cv2
import numpy as np
import math

class HSVstats:

    def __init__(self, image):
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def get_stats(self):
        cv = self.circular_variance()
        return self.mean_s(), self.mean_v(), self.std_s(), self.std_v(), cv

    def mean_s(self):
        return np.mean(self.image[:, :, 1])

    def mean_v(self):
        return np.mean(self.image[:, :, 2])

    def std_s(self):
        return np.std(self.image[:, :, 1])

    def std_v(self):
        return np.std(self.image[:, :, 2])

    def circular_variance(self):
        shp = self.image.shape
        shp = shp[0]*shp[1]
        H = self.image[:, :, 0].reshape(shp)
        A = np.sum(np.cos(H))
        B = np.sum(np.sin(H))
        A **= 2
        B **= 2
        A += B
        R = np.sqrt(A)/shp
        return 1 - R
