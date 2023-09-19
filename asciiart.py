import cv2
import numpy as np
import PIL
import os

PATH = "/Users/rtty/downloads/ryo.jpeg"
terminal_size = os.get_terminal_size()

chars = " .:-=+*#%@"
art = ""

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

width, height = img.shape
# twidth, theight = terminal_size.lines, terminal_size.columns
twidth =  len(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::+*#########################################################################################')
theight = 59

ratio = width / height

x = 3
y = 1.8

blocksize1 = int(width * x / twidth)
blocksize2 = int(height / (y*theight))

# img = cv2.resize(img, (new_height, new_width))

img_float = np.float32(img)
img_normal = cv2.normalize(img_float, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

for i in range(0, width, blocksize1):
    for j in range(0, height, int(blocksize2)):
        pixel = int(img_normal[i, j]*len(chars))
        ascii_char = chars[pixel-1]

        art += ascii_char
    art += '\n'

print(art)

with open('/Users/rtty/documents/code/imgman/asciiart.txt', 'w') as f:
    f.write(art)


cv2.imshow("img", img)

cv2.waitKey(0)

cv2.destroyAllWindows()