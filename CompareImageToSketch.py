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
    

img1=readImage()
img2=readImage()
imgTrain=trainModel(img1)
imgTest=testData(img2)
encodeTrain=encodTrainModel()
encodeTest=encodTestData()
results=face_recognition.compare_faces([encodeTrain],encodeTest)
print("Images to Sketch Comapare Accuracy")
if results==[True]:
    print("Both pictures are match..")
else:
    print("Bothe Pictures are different")
    
faceDis=face_recognition.face_distance([encodeTrain],encodeTest)
print(results,faceDis)

displayImages(imgTest,imgTrain)
cv2.waitKey(0)
