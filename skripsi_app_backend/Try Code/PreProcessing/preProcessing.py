import cv2

image = cv2.imread("../20230529_091443.jpg")

# Crop image to square
height, width, channels = image.shape

if height > width:
    crop_size = width
    y = int((height - width) / 2)
    x = 0
else:
    crop_size = height
    x = int((width - height) / 2)
    y = 0

cropped_image = image[y:y+crop_size, x:x+crop_size]

# Resize image
resized_image = cv2.resize(cropped_image, (256, 256))

cv2.imshow("Cropped Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
