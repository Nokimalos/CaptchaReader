from PIL import Image
from operator import itemgetter

img = Image.open("../captcha/different_pixel_captcha.PNG") #Open the captcha
img = img.convert("L") #Convert image to grayscale
converted_img = Image.new("P", img.size, 255) #Create the output image   

hist = img.histogram() #Do the histogram to see the greatest number of pixels

def putPixelOutpoutImage(addpixel):
    values = {} #Create an array that will store the values
    for i in range(256):
        values[i] = hist[i] #Store the value

    for j in sorted(values.items(), key = itemgetter(1), reverse = True)[addpixel]: #Define a variable between the brackets and increment it each time the AI ​​fails
        #Image path
        for x in range(img.size[1]):
            for y in range(img.size[0]):
                pix = img.getpixel((y,x))# Take the pixel
                if pix == j: # If the pixel is within the range of the greatest number of pixels
                    converted_img.putpixel((y,x),0) #Put the pixel on the new image

    converted_img.save("output.gif") #Save the new image
    return 0


putPixelOutpoutImage(2)