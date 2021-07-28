import cv2
import time
import numpy as np
import mediapipe as mp
import tensorflow as tf
from threading import Thread
from head_pose_ratio import head_pose_ratio
from function import draw_point, eye_avg_ratio, put_text
from Angle_head_pose_ratio import head_pose_status, eye_stat
from mode import sleep_mode
interpreter = tf.lite.Interpreter('model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
cap = cv2.VideoCapture('Video/test_1406.mp4')
# cap = cv2.VideoCapture(0)
pTime = 0
time_active = 0
m = 0
status = ''
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
eye_status = ''
x_status = ''
y_status = ''
z_status = ''
head_status = ''
Drowsy_mode = ''
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
    ih, iw = img.shape[0], img.shape[1]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        Mount = []
        Left_eye = []
        Right_eye = []
        try:
            for face_lms in results.multi_face_landmarks:
                for lm in face_lms.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])

            nose = face[5]
            Left_eye.append([face[249], face[374], face[380], face[382], face[385], face[386]])
            Right_eye.append([face[7], face[145], face[153], face[155], face[158], face[159]])
            Mount.append([face[308], face[317], face[14], face[87], face[61], face[82], face[13], face[312]])
            img = draw_point(img, nose, Left_eye, Right_eye, Mount)
            ear = eye_avg_ratio(Left_eye, Right_eye)
            x1, x2, x3, x4, x5, x6 = head_pose_ratio(nose, Left_eye, Right_eye)
            input_shape = input_details[0]['shape']
            input_data = np.array((x1, x2, x3, x4, x5, x6), dtype=np.float32)
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            img = cv2.putText(img, str(x5), (nose[0] - 20, nose[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            img = cv2.putText(img, str(x6), (nose[0] + 20, nose[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            head_status, mode = head_pose_status(x5, x6, x2)
            eye_status, blink, count = eye_stat(ear, count, blink, mode)
            if mode == 1:
                print(round(ear, 3))

            Drowsy_mode = sleep_mode(mode, ear, blink)
            
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
    key = cv2.waitKey(1)
    # if m == 900:
    #     break
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
