import numpy as np
import cv2
from skimage.feature import greycomatrix

class Main:

    def demo(self):
        img = cv2.imread('images/lena.jpg')
        cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h = img[:, :, 0]
        #piscia = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 2, 2, 2], [2, 2, 3, 3]])
        matrix = greycomatrix(h, [1], [0], levels=256)
        print matrix[:, :, 0, 0]



Main().demo()
