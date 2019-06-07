
# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

import face_recognition
import cv2
import dlib.cuda as cuda
import dlib
import pickle
from pathlib import Path
import db_interface
from PyQt5.QtCore import *

# Display the use of the GPU
print("Number of devices found = ", cuda.get_num_devices())
print("Is dlib use cuda = ", dlib.DLIB_USE_CUDA)

# Set a string for the file path to the pickle folder
directory_in_str = "/home/paul/sdp/pickle_folder"

# Initialize  variables
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
    """The Live Video class to detect and recognise faces"""

    # Set a signal to be emited
    newValue = pyqtSignal(int, int, int, str)

    def __init__(self):
        """Initiase the QObject to alow signals and slots"""
        QObject.__init__(self)

    def run_face(self):
        """Method to launch the camera"""
        # Initialse a variable to access all .pickle files in the pickle folder
        path_list = Path(directory_in_str).glob('**/*.pickle')

        # Initialise variables
        global video_capture
        global video_run
        global unknown_face_encodings
        global unknown_user_count
        video_run = True
        id_usr = 0
        access = 0

        # Clear the encodings
        del known_face_encodings[:]
        del known_face_names[:]
        del users_authority[:]
        del user_id[:]
        del unknown_face_encodings[:]
        del unknown_names[:]
        unknown_user_count = 0

        for nam in unknown_names:
            print("names = ", nam)

        # load each .pickle file to get known person face encodings
        # and add the encodings to the know_faces_encodings array
        # As the loading of the pickle files is not consistent we must
        # make a call to the db for each pickle file loaded
        for path in path_list:
            # because path is object not string
            path_in_str = str(path)
            pickle_in = open(path_in_str, "rb")
            loaded_person = pickle.load(pickle_in)
            # Add the face encoding to the array
            known_face_encodings.append(loaded_person[2])

            print("Pickle id = ", loaded_person[1])
            print("pickle user id = ", loaded_person[4])

            # retrieve the user id info from the db
            user = db_interface.db_id_search(loaded_person[4])
            # Populate the arrays
            for row in user:
                known_face_names.append(row[1])
                users_authority.append(row[4])
                user_id.append(row[0])

        # Get a reference to webcam
        video_capture = cv2.VideoCapture(0)

        # Getting the width and height of the video screen
        w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Loop to consistently run the camera
        while video_run:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Process every frame of video - Can be modified to only process a set number of frames
            if process_this_frame:
                # Find all the face locations and
                face_locations = face_recognition.face_locations(rgb_small_frame)
                # Then create an array of each of the face encodings in the current frame of video
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                # Array to store the names of each face in the frame
                face_names = []
                # Process each detected face in a frame
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    # - creates an array of True and False for each known face encoding
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    # See if the face is a match for the Unknown face(s)
                    # - creates an array of True and False for each Unknown face encoding
                    unknown_matches = face_recognition.compare_faces(unknown_face_encodings, face_encoding)
                    name = "Unknown"
                    access = 0
                    id_usr = 0

                    # If the detected face is neither in the known or Unknown list add it to the Unknown encodings list
                    # Also increase the unknown user count and save this name. I.e - Unknown - 1, Unknown - 2
                    # Both the encoding and name are added to there respective arrays at the same time
                    # so both have matching index values
                    if not any(matches) and not any(unknown_matches):
                        unknown_face_encodings.append(face_encoding)
                        unknown_user_count += 1
                        name = "{} - {}".format(name, unknown_user_count)
                        unknown_names.append(name)

                    # If a match was found in known_face_encodings use the index of the first one to
                    # set the name, access level and user id from the respective lists as
                    # these all match for each person
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                        access = users_authority[first_match_index]
                        id_usr = user_id[first_match_index]

                    # If a match was found in Unknown_face_encodings use the index of the first one to
                    # set the name to the corresponding index in the name array
                    if True in unknown_matches:
                        first_unknown_match_index = unknown_matches.index(True)
                        name = unknown_names[first_unknown_match_index]

                    # Add the resulting name to a temp list. Only used for each detected face in a single frame
                    face_names.append(name)

            # Display the results for each face location and name
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame they were detected on was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Find the middle of the face -
                # Used to detect if the face is in the left or the right side of the screen
                mid = self.mid_point(left, right)

                # Detect if the face is known (access rights between 1 - 3) and on the left of the screen or
                # if the face is on the right side of the screen and has the correct authorisation
                if (mid < (w*0.5) and access > 0) or (mid > (w*0.5) and access > 2):
                    # Draw a Green box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

                    # compute the location of the face
                    loc = 1 if mid < (w*0.5) else 2

                    # Send user info to live_system for table1
                    self.on_changed_value(flag_1, id_usr, loc, name)

                # Detect if a known face is on the right of the screen and
                # doesn't have the correct authorisation to be there
                if mid > (w*0.5) and access < 2:
                    # Draw a Blue box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

                    # Location is set to the right side of the screen
                    loc = 2

                    # Send user info to live_system for table 3
                    self.on_changed_value(flag_3, id_usr, loc, name)

                # Detect if the face is unknown
                if access < 1:
                    # Draw a Red box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

                    # compute the location of the face
                    loc = 1 if mid < (w * 0.5) else 2

                    # Send user info to live_system for table 3
                    self.on_changed_value(flag_2, id_usr, loc, name)

            # Draw the demarcation line in the center of the screen
            cv2.line(frame, (int(w*0.5), 0), (int(w*0.5), int(h)), (0, 255, 0), 2)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit Esc on the keyboard to quit!
            k = cv2.waitKey(1)
            if k % 256 == 27:
                break
        # Call the function to close the video stream and release the camera
        self.end_capture()

    def on_changed_value(self, flag, usr_id, loc, name):
        """Method to emit the signals  to the Home page for the live system tables"""
        self.newValue.emit(flag, usr_id, loc, name)

    def make_connection(self, slider_object):
        """Method to receive a signal"""
        slider_object.changedValue.connect(self.process_signal)

    @pyqtSlot(int)
    def process_signal(self, val):
        """Method to process the received signal"""
        if val == 1:
            self.run_face()
        if val == 2:
            self.end_capture()

    @staticmethod
    def end_capture():
        """Method to end the video processing by setting the video_run variable to False
        - Releasing the camera and destroying the open video feed window"""
        global video_capture
        global video_run

        video_run = False
        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    @staticmethod
    def mid_point(x1, x2):
        """Method to return the mid value between to values"""
        temp = x1+x2

        return temp/2