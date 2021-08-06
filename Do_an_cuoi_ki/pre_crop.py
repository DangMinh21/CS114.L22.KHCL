import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def pre_crop(img, cot_moc):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    # edge detecion
    canny = cv.Canny(gray, 100, 200)
    # cộng hàng với hàng
    def findHori(canny):
        h, w = canny.shape
        array = np.zeros((1, w), dtype = int)
        for i in range(int(h)):
            array[0] = array[0] + canny[i, :]
        return array
    # cộng cột với cột
    def findVer(canny):
        h, w = canny.shape
        array = np.zeros((1, h), dtype = int)
        for i in range(int(w)):
            array[0] = array[0] + canny[:,i]
        return array

    x1 = list(range(canny.shape[1]))
    x1 = np.array(x1)
    x2 = list(range(canny.shape[0]))
    x2 = np.array(x2)
    hori = findHori(canny)
    ver = findVer(canny)
    plt.plot(x1, hori[0])
    plt.plot(x2, ver[0])
    plt.show()
    # dựa vào cột mộc để tìm những tọa độ xung quanh các đỉnh
    def findLandmark(array):
        arr = []
        for i in range(len(array[0])):
            if array[0][i] > cot_moc:
                arr.append(i)
        return arr
    arr_lanmak1 = findLandmark(hori)
    arr_lanmak2 = findLandmark(ver)

    # tìm các đỉnh cũng là tọa độ x, y cần tìm
    def TimToaDo(array, array2):
        point = array[0]
        result = []
        while point <= array[-1]:
            result.append(np.argmax(array2[0][point:point+half_pixel]) + point)
            point += 25
            for i in range(len(array)):
                if array[i] > point:
                    point = array[i]
                    break
        return result

    array1 = TimToaDo(arr_lanmak1, hori)
    array2 = TimToaDo(arr_lanmak2, ver)
    return array1, array2
# lưu tọa độ từng ô vuông vào file .txt
def LuuToaDo(array1, array2, namefile):
    toadotren = []
    toadoduoi = []
    # Tìm tọa độ trên của các ô
    for i in range(len(array2)-1):
        for j in range(len(array1)-12):
            toadotren.append([array1[j], array2[i]])
    for i in range(len(array2)-1):
        for j in range(11, len(array1)-1):
            toadotren.append([array1[j], array2[i]])
    # Tim tọa độ dưới của các ô
    for i in range(1,len(array2)):
        for j in range(1, len(array1)-11): 
            toadoduoi.append([array1[j], array2[i]])
    for i in range(1,len(array2)):
        for j in range(12, len(array1)): 
            toadoduoi.append([array1[j], array2[i]])
    # kết hợp tọa độ trên và tọa độ dưới để có được tọa độ của từng ô rồi lưu vào file .txt
    with open(namefile, 'a') as f:
        for i in range(len(toadotren)):
            toado = str(toadotren[i][0])+' '+str(toadotren[i][1])+' '+str(toadoduoi[i][0])+' '+str(toadoduoi[i][1])+'\n'
            f.write(toado)
if __name__ == '__main__':
    half_pixel =  50
    # id ảnh để cắt
    i = 1
    moc = 100000 
    path = 'data/'
    nameImg = path + str(i) +'.jpg'
    img = cv.imread(nameImg)
    array1, array2 = pre_crop(img, cot_moc=moc)
    namefile = path + str(i) + '.txt'
    LuuToaDo(array1, array2, namefile)







