from PIL import Image
import sys

im = Image.open("captcha.png")
im = im.convert("P") ## Convert the Image to pixels

print (im.histogram())