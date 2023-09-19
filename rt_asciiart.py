import cv2
import numpy as np
import PIL
import os

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

terminal_size = os.get_terminal_size()

chars = " .:-=+*#%@"
art = ""

# twidth, theight = terminal_size.lines, terminal_size.columns
twidth =  len(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::+*#########################################################################################')
theight = 59

# ratio = width / height
x = 1.25
y = 0.8

blocksize1 = int(width / round(width / int(width * x / twidth)))
blocksize2 = int(height / round(height / int(height / (y * theight))))
print(f"Blocksize: {blocksize1} | Width: {width} | Blocks: {width / blocksize1}")
print(f"Blocksize: {blocksize2} | Height: {height} | Blocks: {height / blocksize2}")

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_float = np.float32(img)
    img_normal = cv2.normalize(img_float, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    
    for i in range(0, height, blocksize2):
        for j in range(0, width, blocksize1):
            pixel = int(img_normal[i, j]*len(chars))
            ascii_char = chars[pixel-1]
            art += ascii_char
        art += '\n'

    print(art)
    art = ''


    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
