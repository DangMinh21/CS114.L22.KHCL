import os
import cv2 as cv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

numLetters = 89
pathSou = 'dataResize/'
pathTrain = 'TrainData/'
pathTest = 'TestData/'

Fjoin = os.path.join
images = []
labels = []
# tất cả ảnh
for letter in range(1, numLetters+1):
    pathLetter = pathSou + str(letter) + '/'
    imgList = os.listdir(pathLetter)
    for img in imgList:
        images.append(Fjoin(pathLetter, img))
        labels.append(letter)
# chia data 75% train, 25% test
x_train, x_test, y_train, y_test = train_test_split(images, labels, train_size=0.75, random_state=42)

# lưu data train vào folder train
for i in range(len(y_train)):
    img = cv.imread(x_train[i], 0)
    pathLetterTrain = pathTrain + str(y_train[i]) + '/' + x_train[i].split('/')[-1]
    cv.imwrite(pathLetterTrain, img)

# lưu data test vào folder test
for i in range(len(y_test)):
    img = cv.imread(x_test[i], 0)
    pathLetterTest = pathTest + str(y_test[i]) + '/' + x_test[i].split('/')[-1]
    cv.imwrite(pathLetterTest, img)

# plot_train = pd.Series(y_train).value_counts()
# plot_test = pd.Series(y_test).value_counts()

# fig, axis = plt.subplots(nrows=2, ncols=1, figsize=(18, 8))
# plt.xlabel('89 loại chữ cái khác nhau')
# plt.ylabel('số lượng')
# plt.suptitle('Số lượng từng loại chữ cái')
# axis[0].bar(plot_train.index, plot_train)
# axis[1].bar(plot_test.index, plot_test)
# plt.show()
