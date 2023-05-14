from PIL import Image
from rembg import remove

image = "../image.jpg"
output_image = "../output.jpg"

input = Image.open(image)
output = remove(input)

output.save(output_image)