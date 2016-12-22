import cv2
import numpy as np
import mlpy.wavelet as wave



def get_entropy(image):

    """
            Returns the entropy of the image

            Parameters
            ----------
                image : array_like
                    input image

            Returns
            -------
                out : float
                    the value of the image entropy

    """

    hist = cv2.calcHist(image, [0], None, [256], [0,256])
    #hist /= np.sum(hist)
    div = hist/np.sum(hist)
    log = cv2.log(div)
    return -1 * np.sum(log * hist)


def wavelet_based_textures(image):
    cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = image[:, :, 0]
    sat = image[:, :, 1]
    br = image[:, :, 2]
    wave.dwt(hue, 'd', 3)


def GIST_feature(image):
    cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    




