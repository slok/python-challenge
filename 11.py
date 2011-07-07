import Image
imgPath = '/home/slok/python-challenge/data/cave.jpg'

#load image
im = Image.open(imgPath)
pixels = im.load()

#new image
size = 640, 480
im2 = Image.new("RGB", size, 0)
pixelsOut = im2.load()


odd = False

#get one pixel yes, one no, and add to a new black background RGB image (in grayscale or RGB with white background the word isn't visible)
for y in range(0, 480):
    
    #when we start a new line the pattern yes/no/yes/no... doesnt work (the last one of the previous line is repeated in the first one of the new line)
    if odd == True:
        odd = False
    else:
        odd = True
    
    for x in range(0, 640):
        if odd:
            #add to the new image
            pixelsOut[ x , y ] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2])
            odd = False
        else:
            odd = True


im2.save( '/home/slok/python-challenge/data/CAVEut.jpg', "JPEG")
