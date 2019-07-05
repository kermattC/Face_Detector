import cv2
from tkinter.filedialog import askopenfilename

def detect_faces(frame):
    # convert image to gray scale
    bw_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # search coordinates of image
    faces = face_cascade.detectMultiScale(bw_frame, scaleFactor = 1.05, minNeighbors = 5)

    return faces

# create face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

menu_key = input('Select photo/webcam (enter \'p\' for photo and \'w\' for webcam: ')

if (menu_key == 'p'):
    filename = askopenfilename()
    print('File selected: ', filename)
    
    # read the image
    img = cv2.imread(filename, 1)

    # convert image to gray scale and search coordinates of image
    faces = detect_faces(img)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)

    cv2.imshow('Detected faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif (menu_key == 'w'):
    # create videocapture object via webcam
    # think you might have to change this if you have external webcam
    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()

        # convert each frame to grayscale
        bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # search coordinates of image
        faces = face_cascade.detectMultiScale(bw_frame, scaleFactor = 1.05, minNeighbors = 5)
        
        try:
            if (faces.size > 0):
                print('face detected')
                print(faces)
            # draw rectangle on face
            for x, y, w, h in faces:
                vid = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
        except AttributeError:
            print('no face detected')
            pass
        cv2.imshow('Lord of gay', frame)
    
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
    video.release()

cv2.destroyAllWindows()
