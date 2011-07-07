
import Image
import ImageFilter

#imgPath = '/home/slok/python-challenge/data/evil1.jpg'
imgPath = '/home/slok/python-challenge/data/evil2.gfx'

size = (640, 480)
im2 = Image.new("RGB", size, 0)
pixelsOut = im2.load()

#load image
im = Image.open(imgPath)
pixels = im.load()

for x in range(0,640):
    for y in range(0,480):
        pix = pixels[x, y]
        if pix[0] != 0:
            pixelsOut[x, y] = (pix[0],pix[1],pix[2])
        
#imFilter = im.filter(ImageFilter.MinFilter(1))
#imFilter.save('/home/slok/python-challenge/data/evil1out.jpg', "JPEG") 


im2.save('/home/slok/python-challenge/data/evil1out.jpg', "JPEG") 

print im.info
#print im.info['exif']
