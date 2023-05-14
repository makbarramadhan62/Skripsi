import cv2

image = cv2.imread("../image.jpg")
tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(tmp, 127, 255, cv2.THRESH_BINARY)
mask = cv2.dilate(mask.copy(), None, iterations=10)
mask = cv2.erode(mask.copy(), None, iterations=10)
b, g, r = cv2.split(image)
rgba = [b, g, r, mask]
dst = cv2.merge(rgba, 4)

print(image.shape)
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
