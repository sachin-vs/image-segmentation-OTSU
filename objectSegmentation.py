#segment objects from background
from os import wait
import cv2
import matplotlib.pyplot as plt

def segmentation(img):

    im1=img.copy()
    img=cv2.GaussianBlur(img,(15,15),0)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)==2:
        cnts=cnts[0]
    else:
        cnts=cnts[1]
    for cn in cnts:
        x,y,w,h=cv2.boundingRect(cn)
        cv2.rectangle(im1,(x,y),(x+w,y+h),(36,255,12),2)
    im=cv2.resize(im1,(500,500))
    return im

cv2.imshow('gff',segmentation(cv2.imread('multi2.jpeg')))
cv2.waitKey()