import cv2
import numpy as np
import face_recognition
from PIL import Image
from random import *
import os
#Name:Navdeep Kaur
print("\n\n=================== Face Recognize AI App ============================\n")

def imageList():
    print("\n\t\t List of Test Images\n")
    rec=1
    for filename in os.listdir('images/'):
        if filename.endswith('.jpg'):
            print("\t\t%d). %s"%(rec,filename))
            rec=rec+1
    print("\n\t\t----------------------------\n")

def sketchList():
    print("\n\t\t List of Sketch Images\n")
    rec=1
    for filename in os.listdir('sketches/'):
        if filename.endswith('.jpg'):
            print("\t\t%d). %s"%(rec,filename))
            rec=rec+1
    print("\n\t\t----------------------------\n")

def readImage():
    imgname=input("Enter the Image name without extentions :")
    imgname=imgname+".jpg"
    return imgname
    

def trainModel(img):
    
    imgTrain=face_recognition.load_image_file('images/'+img)
    imgTrain=cv2.cvtColor(imgTrain,cv2.COLOR_BGR2RGB)
    return imgTrain

def testData(img):
    imgTest=face_recognition.load_image_file('sketches/'+img)
    imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
    return imgTest

def encodTrainModel():
    faceLoc=face_recognition.face_locations(imgTrain)[0]
    encodeTrain=face_recognition.face_encodings(imgTrain)[0]
    cv2.rectangle(imgTrain,(faceLoc[3],faceLoc[0],),(faceLoc[1],faceLoc[2]),(255,0,255),2)
    return encodeTrain

def encodTestData():
    faceLocTest=face_recognition.face_locations(imgTest)[0]
    encodeTest=face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0],),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
    return encodeTest

def displayImages(imgTest,imgTrain):
    cv2.putText(imgTest,f'{results},{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('Test Data', imgTest)
    cv2.imshow('Train',imgTrain)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
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

def divide(grey_img, b, invertedblur=256.0):
    return (grey_img * scale) / invertedblur


print("====================Welcome to My Project on Image Processing Compare Sketch to Image Using AI Face Recognition =======================\n")

ch=1
print("\n\t\t Main Menu")
while ch<5:
    print("\t\t1. Image List")
    print("\t\t2. Convert Image to Sketch")
    print("\t\t3  Compare Image to Sketch")
    print("\t\t4. Sketch List")
    print("\t\t.5 Exit")
    print("\t\t----------------------------\n")
    ch=int(input("Enter Choice 1-3 :"))
    if ch==1:
        imageList()
    elif ch==2:
        os.system('python ImageSketch.py') 
        
    elif ch==3:
        os.system('python CompareImageToSketch.py')
       
    elif ch==4:
        sketchList()

