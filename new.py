import cv2
import numpy as np
import face_recognition
# Load BGR image
bgr = cv2.imread(r"dataset2/biden.jpg", cv2.IMREAD_COLOR)

# Convert to RGB
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Ensure 8‑bit per channel
if rgb.dtype != np.uint8:
    if rgb.dtype in (np.float32, np.float64):
        rgb = (rgb * 255).clip(0, 255).astype(np.uint8)
    else:
        rgb = rgb.astype(np.uint8)

# Now rgb is guaranteed to be an 8‑bit RGB image
img_encoding = face_recognition.face_encodings(rgb) 

cv2.imshow("Img", rgb)
cv2.waitKey(0)