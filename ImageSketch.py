import cv2
import numpy as np
import face_recognition
from PIL import Image
from random import *
import os
#Name:Navdeep Kaur

def readImage():
    imgname=input("Enter the Image name without extentions :")
    imgname=imgname+".jpg"
    return imgname

def convertToSketch(img):
    image1 = cv2.imread('images/'+img)
    window_name = 'Original Image'
    cv2.imshow(window_name, image1)
    grey_img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(grey_img)
    blur=cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur=cv2.bitwise_not(blur)
    sketch=cv2.divide(grey_img, invertedblur, scale=256.0)
    return sketch

print("Enter the Image Name you want to convert in skecth :")
img0=readImage()
print(img0)
sketch=convertToSketch(img0)
x=randint(1, 1000)
sname="sketch"+str(x)+".jpg"
print("Sketch File Save in the name of :"+sname)
cv2.imwrite("sketches/"+sname, sketch)
image = cv2.imread("sketches/"+sname)
window_name ='Sketch Image'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
