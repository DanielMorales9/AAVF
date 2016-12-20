import cv2
import numpy as np


class Entropy:

    def __init__(self, image):
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def get_entropy(self):
        hist = cv2.calcHist(self.image, [0], None, [256], [0,256])
        hist /= np.sum(hist)
        log = cv2.log(hist)
        return -1 * np.sum(log * hist)
