import cv2
from tkinter.filedialog import askopenfilename

def nothing(x):
    print(x)

def detect_faces(frame):
    # convert image to gray scale
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # search coordinates of image
    faces = face_cascade.detectMultiScale(bw_frame, scaleFactor = 1.05, minNeighbors = 5)

    return faces

font = cv2.FONT_HERSHEY_SIMPLEX
window_name = 'Face Detector'

# create face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
menu_key = input('Select photo/webcam (enter \'p\' for photo and \'w\' for webcam: ')
# name of window for webcam
cv2.namedWindow('Face Detector')

# create trackbar
cv2.createTrackbar('R', window_name, 0, 255, nothing)
cv2.createTrackbar('G', window_name, 0, 255, nothing)
cv2.createTrackbar('B', window_name, 0, 255, nothing)


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

        # receive values from trackbars
        b_channel = cv2.getTrackbarPos('B', window_name)
        g_channel = cv2.getTrackbarPos('G', window_name)
        r_channel = cv2.getTrackbarPos('R', window_name)

        try:
            if (faces.size > 0):
                print('face detected')
                print(faces)
            # draw rectangle on face
            for x, y, w, h in faces:
                vid = cv2.rectangle(frame, (x,y), (x+w, y+h), (b_channel, g_channel, r_channel), 3)
        except AttributeError:
            print('no face detected')
            pass
        cv2.imshow(window_name, frame)
    
        key = cv2.waitKey(1)
        if key == 27:
            break
        
    video.release()

cv2.destroyAllWindows()