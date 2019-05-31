
# Paul Fetherston
#
# Student No: 2898842

import face_recognition
import cv2
import dlib.cuda as cuda
import dlib
import pickle
from live_system import UILiveSystem
from pathlib import Path
import db_interface
import datetime

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

print("Number of devices found = ", cuda.get_num_devices())

print("Is dlib use cuda = ", dlib.DLIB_USE_CUDA)


directory_in_str = "/home/paul/sdp/pickle_folder"

# Initialize some variables
process_this_frame = True
known_face_encodings = []
known_face_names = []
users_authority = []
user_id = []
video_capture = 0
video_run = True

unknown_face_encodings = []
unknown_names = []
unknown_user_count = 0
unknown_user_name = ''

flag_1 = 1
flag_2 = 2
flag_3 = 3


class LiveVideo(QObject):

    newValue = pyqtSignal(int, int, int, str)

    def __init__(self):
        # Initialize the PunchingBag as a QObject
        QObject.__init__(self)

    def run_face(self):
        path_list = Path(directory_in_str).glob('**/*.pickle')

        global video_capture
        global video_run
        global unknown_face_encodings
        global unknown_user_count
        video_run = True
        id_usr = 0
        access = 0

        for path in path_list:
            # because path is object not string
            path_in_str = str(path)
            pickle_in = open(path_in_str, "rb")
            loaded_person = pickle.load(pickle_in)
            known_face_encodings.append(loaded_person[2])

        records = db_interface.db_retrieve()

        for row in records:
            known_face_names.append(row[1])
            users_authority.append(row[5])
            user_id.append(row[0])

        for name in known_face_names:
            print('name = ', name)
        for acc in users_authority:
            print('access = ', acc)

        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)

        # Getting the width and height of the video screen
        w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while video_run:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    unknown_matches = face_recognition.compare_faces(unknown_face_encodings, face_encoding)
                    name = "Unknown"
                    access = 0
                    id_usr = 0
                    loc = 0


                    # if len(unknown_face_encodings) < 1 and not any(matches):
                    #     print("This is 11111111111111111111111111111111111111111111111111111111111111")
                    #     unknown_face_encodings.append(face_encoding)
                    #     unknown_user_count += 1
                    #     name = "{} - {}".format(name, unknown_user_count)
                    #     unknown_names.append(name)

                    if not any(matches) and not any(unknown_matches):
                        print("This 888888888888888888888888888888888888888888888888888888888888888888888")
                        unknown_face_encodings.append(face_encoding)
                        unknown_user_count += 1
                        name = "{} - {}".format(name, unknown_user_count)
                        unknown_names.append(name)


                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        print("This is 2222222222222222222222222222222222222222222222222222222222222222")
                        first_match_index = matches.index(True)
                        # print("True in matches index location", first_match_index)
                        name = known_face_names[first_match_index]
                        access = users_authority[first_match_index]
                        id_usr = user_id[first_match_index]


                    if True in unknown_matches:
                        print("This is 3333333333333333333333333333333333333333333333333333333333333333333")
                        first_unknown_match_index = unknown_matches.index(True)
                        name = unknown_names[first_unknown_match_index]


                    face_names.append(name)

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                mid = self.mid_point(left, right)

                if (mid < (w*0.5) and access > 0) or (mid > (w*0.5) and access > 2):
                    # Draw a Green box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

                    loc = 1 if mid < (w*0.5) else 2

                    # Send user info to live_system for table1
                    self.on_changed_value(flag_1, id_usr, loc, name)

                if mid > (w*0.5) and access < 2:
                    # Draw a Blue box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

                    loc = 2

                    # Send user info to live_system for table 3
                    self.on_changed_value(flag_3, id_usr, loc, name)

                if access < 1:
                    # Draw a Red box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

                    loc = 1 if mid < (w * 0.5) else 2

                    # Send user info to live_system for table 3
                    self.on_changed_value(flag_2, id_usr, loc, name)

            cv2.line(frame, (int(w*0.5), 0), (int(w*0.5), int(h)), (0, 255, 0), 2)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            k = cv2.waitKey(1)

            # Hit Esc on the keyboard to quit!
            if k%256 == 27:
                break

        self.end_capture()
        # # Release handle to the webcam
        # video_capture.release()
        # cv2.destroyAllWindows()

    def on_changed_value(self, flag, usr_id, loc, name):
        print("Realtime_face +++++++++++++ on_changed_value flag  : ", flag)
        print("Realtime_face +++++++++++++ on_changed_value usr_id  : ", usr_id)
        print("Realtime_face +++++++++++++ on_changed_value loc  : ", loc)
        print("Realtime_face +++++++++++++ on_changed_value name  : ", name)

        self.newValue.emit(flag, usr_id, loc, name)


    def make_connection(self, slider_object):
        print("Realtime_face +++++++++++++ Make_connection : ", slider_object)
        slider_object.changedValue.connect(self.get_slider_value)

    @pyqtSlot(int)
    def get_slider_value(self, val):
        print("Realtime_face ++++++++++++++++ get_slider_value : ", val)
        if val == 1:
            self.run_face()
        if val == 2:
            self.end_capture()


    @staticmethod
    def end_capture():
        global video_capture
        global video_run

        video_run = False
        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    @staticmethod
    def mid_point(x1, x2):
        temp = x1+x2

        return temp/2




