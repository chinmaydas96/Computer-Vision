'''
show stream of only face image in video stream .
 
'''




import numpy as np
import cv2
import sys

 
video_capture = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('19105910_729096427301581_4852294744866713988_n.jpg')
	
while True:

	# Capture frame-by-frame
	ret, img = video_capture.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	crop_img = np.zeros((300, 300, 3), np.uint8)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
		crop_img = img[y:y+h, x:x+w]



	cv2.imshow('Video', crop_img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

		# cv2.resizeWindow('img', 320,240)
		# imgr = cv2.resize(img, (620, 540))
		
video_capture.release()
cv2.destroyAllWindows()

