#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed Nov 28 12:33:08 2018

@author: jordansauchuk
'''


from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import shutil  
import re
import os
import cv2


#folder
if not os.path.exists('image_frames'):
    os.makedirs('image_frames')
 

test_vid = cv2.VideoCapture('Obama.mp4')


#frames 
index = 0
while test_vid.isOpened():
    ret,frame = test_vid.read()
    if not ret:
        break

    #file name
    name = './image_frames/frame' + str(index) + '.png'
    
    if index==20:
        print ('Extracting frames...' + name)
        cv2.imwrite(name, frame)
        break
    
    index = index + 1
    
    
test_vid.release()
cv2.destroyAllWindows()  

#reading image 
demo = Image.open("./image_frames/frame20.png")
text = pytesseract.image_to_string(demo, lang = 'eng')
shutil.rmtree('image_frames')  #deleting folder 
texts=text.split("=")
flag=False;

for i in range(len(texts)):
    if texts[i]=="token":
        flag=True
        token=texts[i+1]
        token=token.replace(" ", "")
        
if flag!=True:
    print("No token found")        














