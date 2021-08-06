import cv2
import numpy as np
import math
import os

pathSou = 'data/'
pathDes = 'dataCrop/'
def cropImg():
    num_of_Img=1
    # crop mắt trước
    for i in range(1, 30, 2):
        nameImage = pathSou + str(i) + '.jpg'
        image = cv2.imread(nameImage)
        nameFile = pathSou + str(i) + '.txt'
        f = open(nameFile)
        index_img=num_of_Img
        # mặt giấy trước(chứa chữ a) lưu trong 44 folder đầu
        index_folder = 0
        for line in f:
                if index_img%10 == 1:
                    index_folder += 1
                    index_img = num_of_Img
                line = line.split()
                x_tren = int(line[0])
                y_tren = int(line[1])
                x_duoi = int(line[2])
                y_duoi = int(line[3])
                saveimg = image[y_tren:y_duoi, x_tren:x_duoi]
                path = pathDes + '/%d/%d.jpg' % (index_folder,index_img)
                cv2.imwrite(path,saveimg)
                index_img += 1
        num_of_Img += 10

    num_of_Img=1
    # crop mặt sau
    for i in range(2, 31, 2):
        nameImage = pathSou + str(i) + '.jpg'
        image = cv2.imread(nameImage)
        nameFile = pathSou + str(i) + '.txt'
        f = open(nameFile)
        index_img=num_of_Img
        #mặt giấy sau lưu trong 45 foldẻ cuối
        index_folder = 44
        for line in f:
                if index_img%10 == 1:
                    index_folder += 1
                    index_img = num_of_Img
                line = line.split()
                x_tren = int(line[0])
                y_tren = int(line[1])
                x_duoi = int(line[2])
                y_duoi = int(line[3])
                saveimg = image[y_tren:y_duoi, x_tren:x_duoi]
                path = pathDes + '%d/%d.jpg' % (index_folder,index)
                cv2.imwrite(path,saveimg)
                index_img += 1
        num_of_Img += 10

if __name__ == '__main__':
    cropImg()