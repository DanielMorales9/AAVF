import cv2
import numpy as np
import math

# Constants
PI = 3.141592653589793

'''
Common class for composition feature extraction
'''


class Composition:
    def __init__(self, image):
        self.image = image

    # canny detection
    def get_canny_image(self, ratio=0.33, min_threshold=None, max_threshold=None):
        # transforming image to gray
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # filter high frequency value from image
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        if min_threshold is None and max_threshold is None:
            v = np.median(blurred)
            min_threshold = int(max(0, (1.0 - ratio) * v))
            max_threshold = int(min(255, (1.0 + ratio) * v))

        # canny edge detection
        edged = cv2.Canny(blurred, min_threshold, max_threshold)
        return edged

    def num_line_edges(self, threshold_ratio=0.33, min_threshold=None, max_threshold=None):
        edged = self.get_canny_image(threshold_ratio, min_threshold, max_threshold)

        # get line edges
        lines = cv2.HoughLinesP(edged, 1, PI / 180, 80)[0]

        # counting number of vertical and horizontal edges
        vertical = 0
        horizontal = 0
        for l in lines:
            if l[0] != l[2] or l[1] != l[3]:
                if self.is_vertical(l):
                    vertical += 1
                else:
                    horizontal += 1

        return vertical, horizontal

    def amount_edge_pixels(self, threshold_ratio=0.33, min_threshold=None, max_threshold=None):
        edged = self.get_canny_image(threshold_ratio, min_threshold, max_threshold)

        edge_pixels = 0.0

        for edge in edged:
            for e in edge:
                if e == 255:
                    edge_pixels += 1

        return edge_pixels / (edged.shape[0] * edged.shape[1]) * 100

    def is_vertical(line):
        hypo = math.sqrt((line[2] - line[0]) ** 2 + (line[3] - line[1]) ** 2)
        opponent = line[3] - line[1]
        sine = opponent / hypo
        sen45 = math.sqrt(2) / 2

        return (not (sine > 1 or not (sine >= sen45))) or (sine >= -1 and not sine > -sen45)
