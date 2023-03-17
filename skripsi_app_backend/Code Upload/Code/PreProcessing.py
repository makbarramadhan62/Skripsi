import cv2

# inisialisasi ukuran resize
width, height = 1080, 1920

# membaca file
img = cv2.imread()
# melakukan resize pada file
img = cv2.resize(img, (width, height),
                 interpolation=cv2.INTER_AREA)
# melakukan cropping pada file
img = img[420:1500, 0:1080]