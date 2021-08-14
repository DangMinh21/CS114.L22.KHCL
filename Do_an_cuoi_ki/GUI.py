from tkinter import *
import tkinter.font as font
from tkinter.filedialog import askopenfilename
import  PIL.ImageGrab as ImageGrab
import cv2
import numpy as np
import pandas as pd
import pickle
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
# from skimage.feature import hog
from PIL import Image, ImageTk

# tải model 
with open("modelNN3.pickle", 'rb') as file_model:
    model = pickle.load(file_model)
with open("scale.pickle", 'rb') as file_scale:
    scale = pickle.load(file_scale)

label = {1: 'a', 2: 'á', 3: 'à', 4: 'ả', 5: 'ạ', 6: 'ã', 7: 'ă', 8: 'ắ', 9: 'ằ', 10: 'ẳ', 11: 'ặ', 12: 'ẵ', 13: 'â', 14: 'ấ', 15: 'ầ', 16: 'ẩ', 17: 'ậ', 18: 'ẫ', 19: 'b', 20: 'c', 21: 'd', 22: 'đ', 23: 'e', 24: 'é', 25: 'è', 26: 'ẻ', 27: 'ẹ', 28: 'ẽ', 29: 'ê', 30: 'ế', 31: 'ề', 32: 'ể', 33: 'ệ', 34: 'ễ', 35: 'g', 36: 'h', 37: 'i', 38: 'í', 39: 'ì', 40: 'ỉ', 41: 'ị', 42: 'ĩ', 43: 'k', 44: 'l', 45: 'm', 46: 'n', 47: 'o', 48: 'ó', 49: 'ò', 50: 'ỏ', 51: 'ọ', 52: 'õ', 53: 'ô', 54: 'ố', 55: 'ồ', 56: 'ổ', 57: 'ộ', 58: 'ỗ', 59: 'ơ', 60: 'ớ', 61: 'ờ', 62: 'ở', 63: 'ợ', 64: 'ỡ', 65: 'p', 66: 'q', 67: 'r', 68: 's', 69: 't', 70: 'u', 71: 'ú', 72: 'ù', 73: 'ủ', 74: 'ụ', 75: 'ũ', 76: 'ư', 77: 'ứ', 78: 'ừ', 79: 'ử', 80: 'ự', 81: 'ữ', 82: 'v', 83: 'x', 84: 'y', 85: 'ý', 86: 'ỳ', 87: 'ỹ', 88: 'ỷ', 89: 'ỵ'}

# tiền sử lý ảnh 
def preprocessing(gray):
    #threshold
    ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
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
            # x_max, y_max, w_max, h_max = x, y, w, h
            # max = cv2.contourArea(cnt)
            x_min = min(x_min, x)
            y_min = min(y_min, y)
            if x + w > x_max:
                x_max = x + w
            if y + h > y_max:
                y_max = y + h    
    letter = gray[y_min:y_max, x_min:x_max]
    return letter
 
class recog_char():
  def __init__(self, root):
    self.root = root
    self.root.title('recognise character')
    self.root.geometry('700x400+500+200')
    self.root.configure(background = 'white')
    self.root.resizable(0,0)

    self.imageframe = LabelFrame(self.root, text='Image', relief=RAISED, bd=5, bg='white')
    self.imageframe.place(x=500, y=50, width=130, height=150)

    self.clearBottum = Button(self.root, text='Clear', bd=4, bg='white', command=lambda : self.canvas.delete('all'), width=8, relief=RAISED)
    self.clearBottum.place(x=0, y=0)

    self.selectImageBottum = Button(self.root, text='Choose', bd=4, bg='white', command=self.imageRecognise, width=8, relief=RAISED)
    self.selectImageBottum.place(x=0, y=30)

    self.RecogniseBottum = Button(self.root, text='Recognise', bd=4, bg='white', command=self.paintRecognise, width=8, relief=RAISED)
    self.RecogniseBottum.place(x=0, y=60)

    self.label1 = Label(self.root, text='paint  ')
    self.label1.place(x = 20, y= 130)
    self.label2 = Label(self.root, text=None, width=2, height=1)
    self.label2.place(x = 20, y= 150)
    self.label3 = Label(self.root, text='image')
    self.label3.place(x = 20, y= 200)
    self.label4 = Label(self.root, text=None, width=2, height=1)
    self.label4.place(x = 20, y= 220)

    self.label5 = Label(self.root, text='paint')
    self.label5.place(x = 80, y= 0)
    self.canvas = Canvas(self.root, bg='white', bd=5, relief=GROOVE, width=350, height=350)
    self.canvas.place(x=80, y=20)
    self.canvas.bind('<B1-Motion>', self.paint)
     
  def paint(self, event):
      x1, y1 = (event.x-2), (event.y-2)
      x2, y2 = (event.x+2), (event.y-2)
      self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black', width=7)

  def paintRecognise(self):
    root.update()
    # lấy tạo độ hình đưuọc vẽ
    x = self.root.winfo_rootx() + self.canvas.winfo_x() + 155
    y = self.root.winfo_rooty() + self.canvas.winfo_y() + 80
    x1 = x + self.canvas.winfo_width() + 60
    y1 = y + self.canvas.winfo_height() + 55
    # cắt ảnh và tiền sử lý
    img = ImageGrab.grab().crop((x, y, x1, y1))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = preprocessing(img)
    img = 255 - cv2.resize(img, (16, 16), interpolation=cv2.INTER_AREA)
    x = img.ravel().reshape(1, -1)
    x = scale.transform(x)
    # dự đoán chữ và in ra màn hình
    predict = model.predict(x)
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    self.label1 = Label(self.root, text=label[predict[0]], width=2, height=1)
    self.label1['font'] = myFont
    self.label1.place(x = 20, y= 150)
   
  def imageRecognise(self):
    # mở thư mục tìm ảnh và show lên màn hình
    imagePath = askopenfilename()
    img = Image.open(imagePath)
    image = ImageTk.PhotoImage(img)
    imageLabel = Label(self.imageframe, image=image)
    imageLabel.image = image
    imageLabel.place(x=0, y=0)
    # đọc ảnh mà tiền sử lý
    img = cv2.imread(imagePath, 0)
    img = preprocessing(img)
    img = 255 - cv2.resize(img, (16, 16), interpolation=cv2.INTER_AREA)
    x = img.ravel().reshape(1, -1)
    x = scale.transform(x)
    # Dự đoán chữ và in ra màn hình
    predict = model.predict(x)
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    self.label2 = Label(self.root, text=label[predict[0]], width=2, height=1)
    self.label2['font'] = myFont
    self.label2.place(x = 20, y= 220)

if __name__ == '__main__':
  root = Tk()
  reg = recog_char(root)
  root.mainloop()