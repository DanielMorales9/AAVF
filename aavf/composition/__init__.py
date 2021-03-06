"""
    This module extracts composition features from images

"""

import numpy as np
import math
import cv2

# Constant
PI = 3.141592653589793


def _get_canny_image(image, ratio=0.33, min_threshold=None, max_threshold=None):
    # transforming image to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # filter high frequency value from image
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    if min_threshold is None and max_threshold is None:
        v = np.median(blurred)
        min_threshold = int(max(0, (1.0 - ratio) * v))
        max_threshold = int(min(255, (1.0 + ratio) * v))

    # canny edge detection
    edged = cv2.Canny(blurred, min_threshold, max_threshold)

    return edged


def vertical_horizontal_edges(image, threshold_ratio=0.33, min_threshold=None, max_threshold=None):
    """
            Returns the number of vertical and horizontal edges in image

            Parameters
            -----------
            image : array_like
                input image

            threshold_ratio : float, optional
                Ratio between max and min threshold.
                Default value is 0.33.
                Mutual use with min and max threshold

            min_threshold : float, optional
                min value for edge detection.
                Default is None.

            max_threshold : float, optional
                max value for edge detection.
                Default is None.

            Returns
            -------
                vertical edges : int
                    number of vertical edges
                horizontal edges : int
                    number of vertical edges

    """
    edged = _get_canny_image(image, threshold_ratio, min_threshold, max_threshold)

    # get line edges
    lines = cv2.HoughLinesP(edged, 1, PI / 180, 80)[0]

    # counting number of vertical and horizontal edges
    vertical = 0
    horizontal = 0

    for l in lines:
        if l[0] != l[2] or l[1] != l[3]:
                if _is_vertical(l):
                    vertical += 1
                else:
                    horizontal += 1

        return vertical, horizontal


def percentage_edge_pixels(self, threshold_ratio=0.33, min_threshold=None, max_threshold=None):
    """
            Returns the amount of edge pixels on total image pixels

            Parameters
            -----------
            image : array_like
                input image
            threshold_ratio : float, optional
                Ratio between max and min threshold.
                Default value is 0.33.
                Mutual use with min and max threshold
            min_threshold : float, optional
                min value for edge detection.
                Default is None.
            max_threshold : float, optional
                max value for edge detection.
                Default is None.

            Returns
            -------
            float
                percentage of edge pixels
    """

    edged = self.get_canny_image(threshold_ratio, min_threshold, max_threshold)

    edge_pixels = sum(x == 255 for x in edged)

    return edge_pixels / ((edged.shape[0] * edged.shape[1]) * 100.0)


def _is_vertical(line):
    hypo = math.sqrt((line[2] - line[0]) ** 2 + (line[3] - line[1]) ** 2)
    opponent = line[3] - line[1]
    sine = opponent / hypo
    sen45 = math.sqrt(2) / 2

    return (not (sine > 1 or not (sine >= sen45))) or \
               (sine >= -1 and not sine > -sen45)


def image_size(image):
    """
        Returns the image_size as the sum of the resolution

        Parameters
        -----------
            image : array_like
                input image

        Returns
        -------
            int
                image size
    """
    return image.shape[0] + image.shape[1]


def rule_of_third(image):
    """
        Average of S, V channels over inner rectangle

        Parameters
        -----------
            image : array_like
                input image in HSV space

        Returns
        -------
            tuple
                average of S and V over inner rectangle
    """
    len_x = image.shape[0]
    len_y = image.shape[1]

    x = len_x/3
    y = len_y/3
    start_y = y
    stop_x = x * 2
    stop_y = y * 2

    sum_s = 0.0
    sum_v = 0.0
    while x < stop_x:
        while y < stop_y:
            sum_s += image[x, y, 1]
            sum_v += image[x, y, 2]
            y += 1
        y = start_y
        x += 1

    xy = (len_x * len_y)

    print sum_s

    f6 = sum_s * 9 / xy
    f7 = sum_v * 9 / xy

    return f6, f7
