from PIL import Image
from operator import itemgetter

im = Image.open("captcha.png") #Open the captcha
im = im.convert("L") #Convert image to grayscale
im2 = Image.new("P",im.size,255) #Create the output image

his = im.histogram() #Do the histogram to see the greatest number of pixels
values = {} #Create an array that will store the values
for i in range(256):
    values[i] = his[i] #Store the value

for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:2]: #Define a variable between the brackets and increment it each time the AI ​​fails
    #Image path
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))# Take the pixel
            if pix == j: # If the pixel is within the range of the greatest number of pixels
                im2.putpixel((y,x),0) #Put the pixel on the new image

im2.save("output.gif") #Save the new image