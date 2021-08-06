import cv2
import numpy as np
import os


def preprocessing(gray):
    #threshold
    ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    #find contours
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    h_, w_ = thresh.shape
    lineContour = []
    #find contours are border
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if x < 5 or y < 5 or x+w > w_-5 or y+h > h_-5 :
            lineContour.append(cnt) 
    #delete contours are border
    cv2.drawContours(thresh,lineContour,-1,(0,0,0),2)
    #detect letter
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    x_min = 10**9
    x_max = 0
    y_min = 10**9
    y_max = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if cv2.contourArea(cnt) > 4:
            x_min = min(x_min, x)
            y_min = min(y_min, y)
            if x + w > x_max:
                x_max = x + w
            if y + h > y_max:
                y_max = y + h      
    letter = gray[y_min:y_max, x_min:x_max]
    return letter
if __name__ == '__main__':
    pathSou = 'dataCrop/'
    pathDes = 'datapreprocess/'
    # duyệt mỗi folder 
    for folder in range(1, 90):
        imgList = os.listdir(pathSou + str(folder))
        # xử lí tất cả ảnh trong folder
        for img in imgList:
            nameImage = pathSou + str(folder) + '/' + img
            imgGray = cv2.imread(nameImage, 0)
            processedImg = preprocessing(imgGray)
            if np.size(processedImg) == 0:
                continue
            else: 
                nameImagePreprocess = pathDes + str(folder) + '/' + img
                cv2.imwrite(nameImagePreprocess, processedImg)
