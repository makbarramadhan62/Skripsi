import cv2

# Load image
img = cv2.imread("../image.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get largest contour (assumed to be the object of interest)
cnt = max(contours, key=cv2.contourArea)

# Get bounding box coordinates of the contour
x, y, w, h = cv2.boundingRect(cnt)

# Get ROI
roi = img[y:y+h, x:x+w]

# Draw bounding box on image
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show image with ROI
cv2.imshow("Image with ROI", img)
cv2.imshow("ROI", roi)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
