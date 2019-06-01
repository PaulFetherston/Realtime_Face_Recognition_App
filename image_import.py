
# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

import face_recognition
import cv2
import numpy as np


def add_user():
    # Variable to return if no image captured
    face_encoding = np.array([0])

    # Get a reference to camera
    video_capture = cv2.VideoCapture(0)

    # Getting the width and height of the video screen
    w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        # Read from the Camera
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # Draw a Green rectangle to indicate where face should be placed
        cv2.rectangle(frame, (int(w * 0.10), int(h * 0.10)), (int(w * 0.90), int(h * 0.90)), (0, 255, 0), 3)
        # Display instructions to quit
        cv2.rectangle(frame, (int(w * 0.25), int(h * 0.80)), (int(w * 0.75), int(h * 0.88)), (255, 0, 0),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "Press 'Esc' to Exit", (int(w * 0.40), int(h * 0.85)), font, 0.5,
                    (0, 0, 0), 1, cv2.LINE_AA)

        # Indicate if no faces are detected
        if len(face_locations) < 1:
            cv2.rectangle(frame, (int(w*0.11), int(h*0.11)), (int(w*.89), int(h*0.89)), (0, 0, 255), 3)
            cv2.rectangle(frame, (int(w*0.25), int(h*0.75)), (int(w*0.75), int(h*0.80)), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, 'No Face Found', (int(w*0.40), int(h*0.79)), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        # Indicate if more than one face is detected
        if len(face_locations) > 1:
            cv2.rectangle(frame, (int(w * 0.11), int(h * 0.11)), (int(w * .89), int(h * 0.89)), (0, 0, 255), 3)
            cv2.rectangle(frame, (int(w * 0.25), int(h * 0.75)), (int(w * 0.75), int(h * 0.80)), (0, 0, 255),
                          cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, 'Too Many Faces Detected', (int(w * 0.30), int(h * 0.78)), font, 0.5, (255, 255, 255),
                        1, cv2.LINE_AA)

        # Indicate when one face is detected
        if len(face_locations) == 1:
            cv2.rectangle(frame, (int(w * 0.25), int(h * 0.80)), (int(w * 0.75), int(h * 0.90)), (0, 255, 0),
                          cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Press 'SPACE BAR' to capture face", (int(w * 0.28), int(h * 0.85)), font, 0.5,
                        (0, 0, 0), 1, cv2.LINE_AA)

        # Display the Video frame
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
            if len(face_locations) == 1:
                print('image_import : space bar pressed 1')
                # Grab a single frame of video
                captured = frame
                # face_encoding = 0
                face_encoding = face_recognition.face_encodings(captured)[0]
                break

    # Release the Camera and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

    # Return the face_encoding
    return face_encoding