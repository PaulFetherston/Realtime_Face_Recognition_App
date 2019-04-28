import face_recognition
import cv2
import pickle


def adduser():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Input user name
    name = input('What is your name?')

    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Face Capture", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            # Grab a single frame of video
            captured = frame
            break

    video_capture.release()

    cv2.destroyAllWindows()

    face_encoding = face_recognition.face_encodings(captured)[0]

    ex_dict = {1: name, 2: face_encoding}

    with open('/home/paul/sdp/pickle_folder/{}.pickle'.format(name), 'wb') as f:
        pickle.dump(ex_dict, f)

    f.close()