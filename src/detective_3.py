import cv2
import numpy as np
import face_recognition
import os

path='ImagesAttendance'
images = []
classNames= []
myList=os.listdir(path)
imgElon = face_recognition.load_image_file("imagebasic/elonmusk.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("imagebasic/ElonTest.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)