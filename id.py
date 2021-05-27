import cv2
import time
import mediapipe as mp
from function import draw_point, eye_avg_ratio, put_text
from head_pose_ratio import head_pose_x, head_pose_y, head_pose_z
from head_pose_status import head_pose_x_status, head_pose_y_status, head_pose_z_status, eye_stat

cap = cv2.VideoCapture(0)
pTime = 0

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
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        faces = []
        Left_eye = []
        Right_eye = []
 
        for face_lms in results.multi_face_landmarks:
            if draw:
                mpDraw.draw_landmarks(img, face_lms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)

        for id, lm in enumerate(face_lms.landmark):
            ih, iw, ic = img.shape
            x, y = int(lm.x * iw), int(lm.y * ih)
            # cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN, 0.4, (0, 0, 255), 1)
            face.append([x, y])

        faces.append(face)
        print(face[28])
        cv2.circle(img, (face[7][0], face[7][1]), 1, (0, 255, 0), 1)
        
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime

    text_fps = 'FPS:' + str(fps)
    cv2.putText(img, text_fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.imshow('results', img)
    
    key = cv2.waitKey(1)
    # if t == 300:
    #     cap.release()
    #     break
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
