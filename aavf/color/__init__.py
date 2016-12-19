"""
    This module extracts color features from images
"""

import numpy as np


def _circular_variance(image):
    shp = image.shape
    rshp = shp[0] * shp[1]
    h = image[:, :, 0].reshape(rshp)
    a = np.sum(np.cos(h))
    b = np.sum(np.sin(h))
    a **= 2
    b **= 2
    a += b
    r = np.sqrt(a) / rshp
    return 1 - r


def basic_color_amount(image, color_labels):
    """
        Returns a percentage list of the basic colors:
        black, blue, brown, grey, green, orange, pink, purple, red, white, yellow

        Parameters
        ----------
            image : matrix
                input image
            color_labels: array
                basic label for each color

        Returns
        -------
            out : ndarray
                percentage of each basic color

    """

    shape = image.shape
    rshpd = image.reshape((shape[0] * shape[1], shape[2]))
    r = np.rint(rshpd[:, 2] / 8).astype(int)
    g = 32 * np.rint(rshpd[:, 1] / 8).astype(int)
    b = 32 * 32 * np.rint(rshpd[:, 0] / 8).astype(int)
    index = r + g + b

    color_amount = np.zeros(11)

    for i in index:
        color_amount[color_labels[i] - 1] += 1
    color_amount = color_amount / index.shape[0] * 100
    return color_amount


def hsv_statistics(image):
    """
        HSV statistics takes an image in HSV space
        and compute some statistics over it

        Parameters
        ----------
            image : matrix
                input image

        Returns
        -------
            out : tuple
                - mean saturation
                - mean brightness
                - std saturation
                - std brightness
                - circular variance
    """
    # mean of Saturation
    mean_s = np.mean(image[:, :, 1])

    # mean of Brightness
    mean_v = np.mean(image[:, :, 2])

    # standard deviation of Saturation
    std_s = np.std(image[:, :, 1])

    # standard deviation of Brightness
    std_v = np.std(image[:, :, 2])

    cv = _circular_variance(image)
    return mean_s, mean_v, std_s, std_v, cv


def pleasure_arousal_dominance(brightness, saturation):
    """
        Returns Pleasure Arousal Dominance values of an image
        given its mean of brightness and saturation

        Parameters
        ----------
            brightness: float
                mean value of brightness
            saturation: float
                mean value of saturation

        Returns
        -------
            out : tuple
                - pleasure : float
                - arousal : float
                - dominance : float
    """

    pleasure = 0.69 * brightness + 0.22 * saturation
    arousal = -0.31 * brightness + 0.60 * saturation
    dominance = -0.76 * brightness + 0.32 * saturation

    return pleasure, arousal, dominance
