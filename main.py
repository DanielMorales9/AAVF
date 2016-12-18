import cv2
from color import Color
from composition import Composition

img = cv2.imread('image/lena.jpg')
color = Color(img);

#color.print_basic_color_amounts()

color.pad();

#comp = Composition(img)

#print comp.num_line_edges()

#print comp.amount_edge_pixels()