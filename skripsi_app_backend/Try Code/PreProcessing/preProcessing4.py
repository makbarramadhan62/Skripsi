import cv2
import numpy as np

# Load image
img = cv2.imread('../image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours and get largest contour (assumed to be the object of interest)
contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)

# Get bounding box coordinates of the contour
x, y, w, h = cv2.boundingRect(cnt)

# Get ROI
roi = img[y:y+h, x:x+w]

# Create a mask of the same size as the image and fill it with zeros (black)
mask = np.zeros(img.shape[:2], np.uint8)

# Define background and foreground models
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Define the rectangle enclosing the object of interest (ROI)
rect = (x, y, w, h)

# Apply GrabCut algorithm to remove background
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Create a mask where non-zero pixels indicate the object (likely foreground)
mask2 = np.where((mask == cv2.GC_FGD) | (
    mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

# Apply the mask to the original image to remove the background
result = cv2.bitwise_and(img, img, mask=mask2)

# Draw bounding box on image
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show original image, ROI, and segmented image
cv2.imshow('Original', img)
cv2.imshow('ROI', roi)
cv2.imshow('Result', result)

# Crop the segmented image using ROI
cropped = result[y:y+h, x:x+w]
cv2.imshow('Cropped', cropped)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
