#We have: an image, the image has some "pixels" that look bad in the image
#           If we get the pixel color nomber (are greys, so RGB is the same numbers)
#           and we get: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
#           then we print the numbers in ASCII and get: integrity

import sys
import Image

imgPath = '/home/slok/python-challenge/data/oxygen.png'

im = Image.open(imgPath)

#the grey points are from pixels [0,43] to [608,43] and their size are 7px
#result = smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

res = [105, 110, 116, 101, 103, 114, 105, 116, 121]

i = 0
pixels = im.load()
while i < 609:
    pix = pixels[i,43]
    sys.stdout.write( chr(pix[0]) )
    i += 7

print '\n------------------------------'

for i in res:
    sys.stdout.write(chr(i))
print '\n'
