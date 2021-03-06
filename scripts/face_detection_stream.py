''' 
    real time face detection.

'''

import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier('stop_sign.xml')

video_capture = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame

    imS = cv2.resize(frame, (920, 680))
    cv2.imshow('Video', imS)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
