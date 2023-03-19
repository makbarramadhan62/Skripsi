import cv2

# # inisialisasi ukuran resize
# width, height = 1080, 1920

# # membaca file
# img = cv2.imread()
# # melakukan resize pada file
# img = cv2.resize(img, (width, height),
#                  interpolation=cv2.INTER_AREA)
# # melakukan cropping pada file
# img = img[420:1500, 0:1080]

image = cv2.imread("../Test_Data/20221027_151539.jpg")

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
