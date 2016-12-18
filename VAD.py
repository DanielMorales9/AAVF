import cv2
import numpy as np

class VAD:

    def __init__(self, image):
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def vad(self, b, s):
        p = 0.69*b + 0.22*s
        a = -0.31*b + 0.60*s
        d = -0.76*b + 0.32*s
        return p, a, d