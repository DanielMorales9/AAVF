import cv2
import numpy as np

COLOR_LABELS_PATH = "file/maxcolor.csv"

COLOR_NAMES = ["black", "blue", "brown", "grey", "green", "orange", "pink",
               "purple", "red", "white", "yellow"]

'''
    Color Class extracts features related to image's color
'''


class Color:
    def __init__(self, image):
        self.image = np.array(image)
        self.color_labels = np.genfromtxt(COLOR_LABELS_PATH)
        self.color_labels = self.color_labels.astype(int)
        self.color_amount = np.zeros(11)

    def get_basic_color_amounts(self):
        if np.sum(self.color_amount) == 0:
            shape = self.image.shape
            self.image = self.image.reshape((shape[0]*shape[1], shape[2]))
            r = np.rint(self.image[:, 2] / 8).astype(int)
            g = 32 * np.rint(self.image[:, 1] / 8).astype(int)
            b = 32 * 32 * np.rint(self.image[:, 0] / 8).astype(int)

            im_index = r + g + b
            for i in im_index:
                self.color_amount[self.color_labels[i] - 1] += 1
            self.color_amount = self.color_amount / im_index.shape[0] * 100
        return self.color_amount

    def pad(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        p = 0.69*img[: , : , 2]
        print p



    def print_basic_color_amounts(self):
        self.get_basic_color_amounts()
        for c, i in zip(COLOR_NAMES, self.color_amount):
            print("Percentage of %s: %0.5f " % (c, i))
