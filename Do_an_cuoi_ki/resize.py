import os
import cv2 as cv

numLetters = 89
pathSou = 'datapreprocess/'
pathDes = 'dataResize/'

# resize ảnh về 16x16 gray
for letter in range(1, numLetters+1):
    nameFolderSou = pathSou + str(letter)
    nameFolderDes = pathDes + str(letter)
    ImgList = os.listdir(nameFolderSou)
    for nameImg in range(len(ImgList)):
        pathImgSou = nameFolderSou + '/' + ImgList[nameImg]
        img = cv.imread(pathImgSou, 0)
        imgResize = cv.resize(img, (16, 16), interpolation=cv.INTER_AREA)
        pathImgDes = nameFolderDes + '/' + str(nameImg) + '.jpg'
        cv.imwrite(pathImgDes, imgResize)


