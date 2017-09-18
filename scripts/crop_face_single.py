'''
crop image with argument of image name without extension. 

'''






import numpy as np
import cv2
import os
import argparse
from os import listdir
 

parser = argparse.ArgumentParser()
parser.add_argument("name",type=str)
args = parser.parse_args()
image = args.name + ".jpg"


def face_crop(image):

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# sub_face =  np.zeros((300, 300, 3), np.uint8) 

	for (x,y,w,h) in faces:

		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
		sub_face = img[y:y+h, x:x+w]

	# face_file_name = "image_"+ str(i) + ".jpg"
	# cv2.imwrite(face_file_name, sub_face)
	#img = cv2.resize(img, (920, 680))
	cv2.imshow('img',img)
	return 

face_crop(image)
cv2.waitKey(0)
cv2.destroyAllWindows()