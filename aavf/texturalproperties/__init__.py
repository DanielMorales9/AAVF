import cv2
import numpy as np
import mlpy.wavelet as wave
from skimage.feature import greycomatrix, greycoprops



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

# todo
def wavelet_based_textures(image):
    cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = image[:, :, 0]
    sat = image[:, :, 1]
    br = image[:, :, 2]
    wave.dwt(hue, 'd', 3)



def GLCM_feature(image):
    cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = image[:, :, 0]
    sat = image[:, :, 1]
    br = image[:, :, 2]
    h_glcm = greycomatrix(hue, [1], [0])
    s_glcm = greycomatrix(sat, [1], [0])
    b_glcm = greycomatrix(br, [1], [0])

    h_cont = greycoprops(h_glcm, prop='contrast')
    s_cont = greycoprops(s_glcm, prop='contrast')
    b_cont = greycoprops(b_glcm, prop='contrast')

    h_corr = greycoprops(h_glcm, prop='correlation')
    s_corr = greycoprops(s_glcm, prop='correlation')
    b_corr = greycoprops(b_glcm, prop='correlation')

    h_ener = greycoprops(h_glcm, prop='energy')
    s_ener = greycoprops(s_glcm, prop='energy')
    b_ener = greycoprops(b_glcm, prop='energy')

    h_homo = greycoprops(h_glcm, prop='homogeneity')
    s_homo = greycoprops(s_glcm, prop='homogeneity')
    b_homo = greycoprops(b_glcm, prop='homogeneity')

    return h_cont, s_cont, b_cont, h_corr, s_corr, b_corr, h_ener, s_ener, b_ener, h_homo, s_homo, b_homo




