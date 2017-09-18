'''
crop image of all the current folders with jpeg file extension.

'''



import numpy as np
import cv2
import sys
import os
from os import listdir
 
def face_crop(image,i):

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	sub_face =  np.zeros((300, 300, 3), np.uint8) 

	for (x,y,w,h) in faces:

		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),4)
		sub_face = img[y:y+h, x:x+w]

	face_file_name = "image_"+ str(i) + ".jpg"
	cv2.imwrite(face_file_name, sub_face)
	# cv2.imshow('img',sub_face)
    
	# cv2.resizeWindow('img', 320,240)
	# imgr = cv2.resize(img, (620, 540))

	return 


relevant_path = "."
included_extensions = ['jpg']
file_names = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]

fnames = listdir(relevant_path)
for i,fname in enumerate(file_names):
	face_crop(fname,i+1)




