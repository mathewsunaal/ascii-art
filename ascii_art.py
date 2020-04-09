from PIL import Image
import numpy as np
import os, glob

# ASCII_CHARS below is arragned in order of thin to thick strokes. This will help map intensity of image to weight of character strokes
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255
NUM_OF_BANDS = 3
THUMBNAIL_SIZE = 300,300 #define the size of thumbnails to create

def create_thumbnails(images_path):
    for image_file in glob.glob(images_path+"*.jpg"):
        file, ext = os.path.splitext(image_file)
        print(file, ext)
        im = Image.open(image_file)
        im.thumbnail(THUMBNAIL_SIZE)
        im.save(image_file + ".thumbnail", "JPEG")

def get_info(image):
    print("The ASCII character array size = ", len(ASCII_CHARS))
    print("The number of bands in the image = ", NUM_OF_BANDS)
    print("The maximum pixel value =", MAX_PIXEL_VALUE)
    print("Columns in the image = ", im1.size[0])
    print("Rows in the image = ", im1.size[1])
    print("Image format = ", im1.format)
    print("Image mode = ", im1.mode)


def get_pixel_matrix(img,xSize,ySize):
    imageArray = np.asarray(img)
    newPixelArray= []
    for i in range(ySize):
        newValRow = []
        for j in range(xSize):
            newValRow.append(sum(imageArray[i,j])/NUM_OF_BANDS)
        newPixelArray.append(newValRow)
    return(newPixelArray)

#mapAsciiArray creates an array with the corresponding ascii indexes based on the calculated brightness value of each pixel    
def map_to_ascii_matrix(pixelArray,xSize,ySize):
    ascii_array_size = len(ASCII_CHARS)
    asciiArray = []
    for i in range(ySize):
        newValRow = []
        for j in range(xSize):
            charMapIndex = ((ascii_array_size*pixelArray[i][j])/MAX_PIXEL_VALUE) - 1
            newValRow.append(ASCII_CHARS[charMapIndex])
        asciiArray.append(newValRow)
    return(asciiArray)

def print_ascii_matrix(asciiArray,xSize,ySize,print_mode='console'):
    error=0
    f = open('output_image.txt', 'w')
    for row in asciiArray:
        line = [p+p for p in row] #ASCII characters are taller by default so print character 2x times to approximate one pixel
        if print_mode == 'console':
            print("".join(line))
        elif print_mode == 'text_file':
            f.write("".join(line))
        else:
            if (error==0):
                print("Invalid print mode requested")
                error=1
        f.write("\n")
    f.close()

########### main()
images_path = str(os.getcwd()+'/images/')
create_thumbnails(images_path)

im1 = Image.open(images_path+'image2.jpg.thumbnail')
xSize = im1.size[0]
ySize = im1.size[1]
get_info(im1) #print info about the image and system

imgData = get_pixel_matrix(im1,xSize,ySize) #parese image and calculate new brightness value for each pixel
asciiArray = map_to_ascii_matrix(imgData,xSize,ySize) #map ascii characters to new pixel array
print_ascii_matrix(asciiArray,xSize,ySize,'text_file') #print the ascii art in console or text file 
