from PIL import Image

im = Image.open('center/center3.png')
print(im.format, im.size, im.mode)
im.show()