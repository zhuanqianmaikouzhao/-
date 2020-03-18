import tesserocr
from PIL import Image
image = Image.open(r'C:\Users\Administrator\image.png')
print(tesserocr.image_to_text(image))
