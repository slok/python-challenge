
#we have: various images (gif, jpg...) and one is gfx, in the gfx file there are 5 images
#           this images are shuffeled, so we have to cut in 5 pieces that .gfx and make 5 images
#           (one hint maybe for the next level is 'bert is evil' chan chan! )
#Solution: disproportional

#unshuffle the 5 images from evil2.gfx
trollImagePath = '/home/slok/python-challenge/data/evil2.gfx'
trollImg = open(trollImagePath, 'r')
trollImg = trollImg.read()
cont = 0
imgList =  ['','','','','']
cont2 = 0
for i in trollImg:
    if cont > 4:
        cont = 0
    imgList[cont] += i
    cont += 1

#save the 5 images
imgPath = '/home/slok/python-challenge/data/'
imgNames = ['img1', 'img2', 'img3', 'img4', 'img5']
imgExt= ['jpg', 'png', 'gif', 'png', 'jpg']
cont = 0

for i in imgList:
    f = open(imgPath + imgNames[cont] +'.'+ imgExt[cont], 'wb')
    f.write(i)
    f.close()
    cont += 1


