#!/usr/bin/python3
import cv2
import time
import mediapipe as mp
from function import draw_point, eye_avg_ratio, put_text
from head_pose_ratio import head_pose_ratio, head_pose_y, head_pose_z
from head_pose_status import head_pose_x_status, head_pose_y_status, head_pose_z_status, eye_stat

cap = cv2.VideoCapture('Video/test.mp4')
pTime = 0
m = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
eye_status = ''
x_status = ''
y_status = ''
z_status = ''
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
    img = cv2.resize(img, (720, 405))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        Left_eye = []
        Right_eye = []
        try:
            for face_lms in results.multi_face_landmarks:
                if draw:
                    mpDraw.draw_landmarks(img, face_lms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)

            for lm in face_lms.landmark:
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                face.append([x, y])


            nose = face[5]

            Left_eye.append([face[249], face[374], face[380], face[382], face[385], face[386]])
            Right_eye.append([face[7], face[145], face[153], face[155], face[158], face[159]])

            img = draw_point(img, nose, Left_eye, Right_eye)
            ear = eye_avg_ratio(Left_eye, Right_eye)
            x1, x2 = head_pose_ratio(nose, Left_eye, Right_eye)
            head_pose_y_ratio = head_pose_y(nose, Left_eye, Right_eye)
            avg_ratio = head_pose_z(nose, Left_eye, Right_eye)
            print(x1)
            y_status = head_pose_y_status(head_pose_y_ratio)
            eye_status, blink, count = eye_stat(ear, count, blink)
        except:
            eye_status = 'None Face'
            x_status = 'None Face'
            y_status = 'None Face'
            blink = 0
            ear = 0
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime
    img = cv2.putText(img, str(m), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    m+=1
    text_fps = 'FPS:' + str(fps)
    text_EaR = 'Eye_avg_Ratio: ' + str(round(ear, 2))
    text_Head_pose_y = 'Head_pose: ' + x_status + ' ' + y_status
    text_ES = 'Eye_Status: ' + eye_status
    text_blink = 'Blink_Num: ' + str(blink)
    text_blink_avg = 'Blink_AVG: ' + str(blink_perM)

    img = put_text(img, text_fps, text_EaR, text_ES, text_blink, text_blink_avg, text_Head_pose_y)
    cv2.imshow('results', img)
    # print(time.time() - start_time)
    if (time.time() - start_time) > 60:
        start_time = time.time()
        blink_perM = blink
        pre_blink = blink
        blink = 0
    key = cv2.waitKey(1)
    # if t == 300:
    #     cap.release()
    #     break
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
