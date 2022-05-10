'''
  ________.__  __  .__         ___.                                  /\        __________              ___________   .__
 /  _____/|__|/  |_|  |__  __ _\_ |__       ____  ____   _____      / / ___  __\______   \ ___________/   _____/  | _|__|
/   \  ___|  \   __\  |  \|  |  \ __ \    _/ ___\/  _ \ /     \    / /  \  \/  /|     ___// __ \_  __ \_____  \|  |/ /  |
\    \_\  \  ||  | |   Y  \  |  / \_\ \   \  \__(  <_> )  Y Y  \  / /    >    < |    |   \  ___/|  | \/        \    <|  |
 \______  /__||__| |___|  /____/|___  / /\ \___  >____/|__|_|  / / /    /__/\_ \|____|    \___  >__| /_______  /__|_ \__|
        \/              \/          \/  \/     \/            \/  \/           \/              \/             \/     \/
'''

from multiprocessing.sharedctypes import Value
import cv2  # Computer Vision 2
from random import randrange
from cv2 import FONT_HERSHEY_SIMPLEX
from cv2 import rectangle
from pygrabber.dshow_graph import FilterGraph
from SETTINGS import *

graph = FilterGraph()
print(graph.get_input_devices())  # list of camera devices

try:
    camera = int(input('Select camera: '))
    camera -= 1
except ValueError:
    camera = 0
    pass

# Load pre-trained detectors
face_data = cv2.CascadeClassifier(face_data)
smile_data = cv2.CascadeClassifier(smile_data)
upperbody_data = cv2.CascadeClassifier(upperbody_data)
eye_data = cv2.CascadeClassifier(eye_data)

# Capture video
webcam = cv2.VideoCapture(camera)

while True:
    frame_read, frame = webcam.read()
    if mirror == True:
        frame = cv2.flip(frame, 1)

    # Convert to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face
    face_coords = face_data.detectMultiScale(
        grayscale,
        scaleFactor=face_scaleFactor,
        minNeighbors=face_minNeighbors,
        minSize=(50, 50)
    )

    # Draw rectangle around face
    for (x, y, w, h) in face_coords:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5)

        cv2.putText(
            frame,
            f'X[{face_coords[0][0]}] Y[{face_coords[0][1]}] W[{face_coords[0][2]}] H[{face_coords[0][3]}]',
            (x, y-50),
            fontScale=0.5,
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            color=(255, 255, 255),
            thickness=1
        )

        # Detect smile
        smile_coords = smile_data.detectMultiScale(
            grayscale,
            scaleFactor=smile_scaleFactor,
            minNeighbors=smile_minNeighbors,
        )

        for (sx, sy, sw, sh) in smile_coords:
            # cv2.rectangle(frame, (sx, sy), ((sx + sw),
            #               (sy + sh)), (0, 0, 255), 2)

            cv2, rectangle(frame, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

            cv2.putText(frame, 'Smiling', (sx, sy),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(255, 255, 255), fontScale=0.5)

        # upperbody_coords = upperbody_data.detectMultiScale(
        #     grayscale,
        #     scaleFactor=1.5,
        #     minNeighbors=5
        # )

        # for (ux, uy, uw, uh) in upperbody_coords:
        #     cv2.rectangle(frame, (ux, uy), ((ux + uw),
        #                   (uy + uh)), (0, 255, 0), 2)

        #     cv2.putText(frame, 'Upperbody', (ux, uy+300),
        #                 fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(255, 255, 255), fontScale=0.5)

        # Detect eyes
        eye_coords = eye_data.detectMultiScale(
            grayscale,
            scaleFactor=eye_scaleFactor,
            minNeighbors=eye_minNeighbors,
        )

        for (ex, ey, ew, eh) in eye_coords:
            cv2.rectangle(frame, (ex, ey), ((ex + ew),
                          (ey + eh)), (0, 255, 0), 2)

            cv2.putText(frame, 'Eye', (ex, ey),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(255, 255, 255), fontScale=0.5)

    # Show frame
    cv2.imshow('Webcam', frame)
    key = cv2.waitKey(1)  # Auto hit key every 1ms

    if key == stop_key:  # if [Esc] key is pressed
        break   # break the loop

print('Video Capture Ended')
