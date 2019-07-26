import cv2
import numpy as np
from tkinter.filedialog import askopenfilename

# color values:
        # blue (5 dollar bill): Lower: 58, 48, 85. Upper: 158, 255, 255

def print_value(x):
    print(x)

def detect_faces(frame):
    # convert image to gray scale
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # search coordinates of image
    faces = face_cascade.detectMultiScale(bw_frame, scaleFactor = 1.05, minNeighbors = 5)

    return faces

font = cv2.FONT_HERSHEY_SIMPLEX
main_window_name = 'Face Detector'
filter_window_name = 'Color Filter'

# create face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
menu_key = input('Select photo/webcam (enter \'p\' for photo and \'w\' for webcam: ')

# name of windows
cv2.namedWindow('Face Detector')
cv2.namedWindow('Color Filter')

# create trackbar
cv2.createTrackbar('R', main_window_name, 0, 255, print_value)
cv2.createTrackbar('G', main_window_name, 0, 255, print_value)
cv2.createTrackbar('B', main_window_name, 0, 255, print_value)
cv2.createTrackbar('Lower_Hue', filter_window_name, 0, 255, print_value)
cv2.createTrackbar('Lower_Sat', filter_window_name, 0, 255, print_value)
cv2.createTrackbar('Lower_Val', filter_window_name, 0, 255, print_value)
cv2.createTrackbar('Upper_Hue', filter_window_name, 0, 255, print_value)
cv2.createTrackbar('Upper_Sat', filter_window_name, 0, 255, print_value)
cv2.createTrackbar('Upper_Val', filter_window_name, 0, 255, print_value)


if (menu_key == 'p'):
    filename = askopenfilename()
    print('File selected: ', filename)
    
    # read the image
    img = cv2.imread(filename, 1)

    # convert image to gray scale and search coordinates of image
    faces = detect_faces(img)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)
        img = cv2.putText(img, 'Face', (x,y), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('Detected faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif (menu_key == 'w'):
    # create videocapture object via webcam
    # you might have to change this if you have external webcam
    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()
        faces = detect_faces(frame)
        # convert frames into hsv images
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        # receive values from trackbars
        b_channel = cv2.getTrackbarPos('B', main_window_name)
        g_channel = cv2.getTrackbarPos('G', main_window_name)
        r_channel = cv2.getTrackbarPos('R', main_window_name)

        lower_hue = cv2.getTrackbarPos('Lower_Hue', filter_window_name)
        lower_sat = cv2.getTrackbarPos('Lower_Sat', filter_window_name)
        lower_val = cv2.getTrackbarPos('Lower_Val', filter_window_name)
        upper_hue = cv2.getTrackbarPos('Upper_Hue', filter_window_name)
        upper_sat = cv2.getTrackbarPos('Upper_Sat', filter_window_name)
        upper_val = cv2.getTrackbarPos('Upper_Val', filter_window_name)

        # store lower and upper hsv values into np arrays
        lower = np.array([lower_hue, lower_sat, lower_val])
        upper = np.array([upper_hue, upper_sat, upper_val])

        # threshold the hsv image of the selected values
        mask = cv2.inRange(hsv_frame, lower, upper)

        # mask original image using bitwise operation
        result = cv2.bitwise_and(frame, frame, mask=mask)

        try:
            if (faces.size > 0):
                print('face detected')
                print(faces)
            # draw rectangle on face
            for x, y, w, h in faces:
                vid = cv2.rectangle(frame, (x,y), (x+w, y+h), (b_channel, g_channel, r_channel), 3)
                vid = cv2.putText(frame, 'Face', (x,y), font, 1, (b_channel, g_channel, r_channel), 1, cv2.LINE_AA)
        except AttributeError:
            print('no face detected')
            pass

        # display windows
        cv2.imshow(main_window_name, frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', result)

        # exit program when user presses esc key
        key = cv2.waitKey(1)
        if key == 27:
            break
        
    video.release()

cv2.destroyAllWindows()