import cv2
import time
import numpy as np
import mediapipe as mp
import tensorflow as tf
from queue import Queue
from tensorflow import keras
from threading import Thread
from head_pose_ratio import head_pose_ratio
from function import draw_point, eye_avg_ratio, put_text, predict
from Angle_head_pose_ratio import head_pose_status, eye_stat
from mode import sleep_mode
<<<<<<< HEAD
class VideoStream:
    """Camera object that controls video streaming"""
    def __init__(self,resolution=(1080,720),framerate=30):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
            
        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

	# Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
	# Start the thread that reads frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
	# Return the most recent frame
        return self.frame

    def stop(self):
	# Indicate that the camera and thread should be stopped
        self.stopped = True



cap = cv2.VideoCapture(0)
=======
model = keras.models.load_model("keras_model.h5")
cap = cv2.VideoCapture('Video/test_1406.mp4')
# cap = cv2.VideoCapture(0)
>>>>>>> e6957c5ecca9f43cc99051af76e29c46a26cd049
pTime = 0
time_active = 0
m = 0
status = ''
y_predict = Queue()
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
mpPose = mp.solutions.pose
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
eye_status = ''
x_status = ''
y_status = ''
z_status = ''
head_status = ''
draw = False
t = 0
ear = 0
start_time = time.time()
count = 0
blink = 0
blink_perM = 0
pre_blink = 0
while True:
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        Mount = []
        pose_xy = []
        Left_eye = []
        Right_eye = []
        try:
            for face_lms in results.multi_face_landmarks:
                for lm in face_lms.landmark:
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])

            nose = face[5]
            Left_eye.append([face[249], face[374], face[380], face[382], face[385], face[386]])
            Right_eye.append([face[7], face[145], face[153], face[155], face[158], face[159]])
            Mount.append([face[308], face[317], face[14], face[87], face[61], face[82], face[13], face[312]])
            img = draw_point(img, nose, Left_eye, Right_eye, Mount)
            ear = eye_avg_ratio(Left_eye, Right_eye)
            x1, x2, x3, x4, x5, x6 = head_pose_ratio(nose, Left_eye, Right_eye)
            img = cv2.putText(img, str(x5), (nose[0] - 20, nose[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            img = cv2.putText(img, str(x6), (nose[0] + 20, nose[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            head_status, mode = head_pose_status(x5, x6, x2)
            eye_status, blink, count = eye_stat(ear, count, blink, mode)
            if mode == 1:
                print(round(ear, 3))

            if mode == 9:
                print("x1:"+str(x1)+ " " + "x2:"+str(x2)+ " " + "x3:"+str(x3)+ " " + "x4:"+str(x4)+ " " + "x5:"+str(x5)+ " " + "x6:"+str(x6))

            m += 1

        except:
            eye_status = 'None Face'
            x_status = 'None Face'
            y_status = 'None Face'
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime
    img = cv2.putText(img, str(m), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    text_fps = 'FPS:' + str(fps)
    text_EaR = 'Eye_avg_Ratio: ' + str(round(ear, 2))
    text_Head_pose = 'Head_pose: ' + head_status
    text_ES = 'Eye_Status: ' + eye_status
    text_blink = 'Blink_Num: ' + str(blink)
    text_blink_avg = 'Blink_AVG: ' + str(blink_perM)
    img = put_text(img, text_fps, text_EaR, text_ES, text_blink, text_blink_avg, text_Head_pose)
    cv2.imshow('results', img)
    if (time.time() - start_time) > 60:
        start_time = time.time()
        time_active += 1
        blink_perM = blink
        pre_blink = blink
        blink = 0
    key = cv2.waitKey(10)
    # if m == 900:
    #     break
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
