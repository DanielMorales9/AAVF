import cv2
from color import Color
from composition import Composition
from HSVstats import HSVstats
from VAD import VAD

img = cv2.imread('image/lena.jpg')
vad = VAD(img)

#color.print_basic_color_amounts()

#color.pad();

#comp = Composition(img)

#print comp.num_line_edges()

#print comp.amount_edge_pixels()

hsv = HSVstats(img)

stats = hsv.get_stats()

print vad.vad(stats[1], stats[0])