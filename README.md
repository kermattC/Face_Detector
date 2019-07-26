# Face_Detector
OpenCV face detection program. You can choose to have the program detect faces from a photo or from your webcam.  

Latest update:
Something wrong with tkinter, unable to use the file selector at the moment. 

Work in progress:
You might have to change the number at line 65 if you are using an external webcam  
(ie: video = cv2.VideoCapture(0) -> video = cv2.VideoCapture(1) OR video cv2.VideoCapture(-1)  

Not sure if hsv color picker works 100%, the webcam I'm using has some kind of blue tint

Packages you have to install:  
OpenCV: pip install opencv-python  
Tkinter: pip install python-tk  

if pip doesn't work use pip3 instead.  
