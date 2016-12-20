import cv2
from Color.HSVstats import HSVstats
from Color.VAD import VAD
from Color.color import Color
from Compositon.composition import Composition
from TexturalProperties.entropy import Entropy

img = cv2.imread('image/gufo.jpg')
vad = VAD(img)

#color.print_basic_color_amounts()

#color.pad();

#comp = Composition(img)

#print comp.num_line_edges()

#print comp.amount_edge_pixels()

hsv = HSVstats(img)

stats = hsv.get_stats()

ent = Entropy(img)


print vad.vad(stats[1], stats[0])
print ent.get_entropy()
