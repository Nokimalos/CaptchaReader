import sys
import os.path

from PIL import Image
from operator import itemgetter

HELP = "USAGE = The first argument is the execution binary of the program.\n"\
    "\tThe second argument is the path of the captcha for the Captcha reader.\n"\
    "EXECUTION = python3 elevator [path of the captcha : \"../captcha/different_pixel_captcha.PNG\"]\n"\

BAD_ARG = "There can only be 2 arguments ! Please do : python3 CaptchaReader \"-help\" for more informations.\n"\

FILE_NOT_FOUND = "This file doesn't exist ! Please retry with a functionnal Captcha.\n"\
    
EMPTY_FILE = "This file is empty ! Please try with a good captcha.\n"\

def putPixelOutpoutImage(addpixel, img, converted_img, hist):
    values = {} #Create an array that will store the values
    for i in range(256):
        values[i] = hist[i] #Store the value

    for j,k in sorted(values.items(), key = itemgetter(1), reverse = True)[:addpixel]: #Define a variable between the brackets and increment it each time the AI ​​fails
        #Image path
        for x in range(img.size[1]):
            for y in range(img.size[0]):
                pix = img.getpixel((y,x)) # Take the pixel
                if pix == j: # If the pixel is within the range of the greatest number of pixels
                    converted_img.putpixel((y,x),0) #Put the pixel on the new image

    converted_img.save("output.gif") #Save the new image
    return 0

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "-help":
        print(HELP)
    elif len(sys.argv) != 2:
        print(BAD_ARG)
    else:
        if (os.path.isfile(sys.argv[1]) == False):
            print(FILE_NOT_FOUND)
        elif (os.path.isfile(sys.argv[1]) == True and os.path.getsize(sys.argv[1]) > 0):
            img = Image.open(sys.argv[1]) #Open the captcha
            img = img.resize((400,100)) #Resize the image
            img = img.convert("L") #Convert image to grayscale
            converted_img = Image.new("P", img.size, 255) #Create the output image
            hist = img.histogram() #Do the histogram to see the greatest number of pixels

            putPixelOutpoutImage(2, img, converted_img, hist)
        else:
            print(EMPTY_FILE)