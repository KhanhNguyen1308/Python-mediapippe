import cv2
import numpy as np


def mid_point(p1, p2):
    mp = (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    return mp


def dist(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a-b)


def draw_point(img, nose, left_eye, right_eye):

    l_m = mid_point(left_eye[0][0], left_eye[0][3])
    r_m = mid_point(right_eye[0][0], right_eye[0][3])

    l_m_sym_x = (l_m[0], nose[1])
    r_m_sym_x = (r_m[0], nose[1])

    l_m_sym_y = (nose[0], l_m[1])
    r_m_sym_y = (nose[0], r_m[1])

    cv2.circle(img, l_m, 1, (0, 255, 0), 1)
    cv2.circle(img, r_m, 1, (0, 255, 0), 1)
    cv2.circle(img, l_m_sym_x, 1, (0, 255, 0), 1)
    cv2.circle(img, r_m_sym_x, 1, (0, 255, 0), 1)
    cv2.circle(img, l_m_sym_y, 1, (0, 255, 0), 1)
    cv2.circle(img, r_m_sym_y, 1, (0, 255, 0), 1)

    cv2.circle(img, nose, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][0], 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][1], 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][2], 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][3], 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][4], 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye[0][5], 1, (0, 255, 0), 1)

    cv2.circle(img, right_eye[0][0], 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye[0][1], 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye[0][2], 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye[0][3], 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye[0][4], 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye[0][5], 1, (0, 255, 0), 1)

    cv2.line(img, left_eye[0][0], left_eye[0][3], (0, 255, 255), 1)
    cv2.line(img, left_eye[0][5], left_eye[0][1], (0, 255, 255), 1)
    cv2.line(img, left_eye[0][4], left_eye[0][2], (0, 255, 255), 1)

    cv2.line(img, right_eye[0][0], right_eye[0][3], (0, 255, 255), 1)
    cv2.line(img, right_eye[0][5], right_eye[0][1], (0, 255, 255), 1)
    cv2.line(img, right_eye[0][4], right_eye[0][2], (0, 255, 255), 1)

    cv2.line(img, (nose[0], 0), (nose[0], 720), (0, 255, 255), 1)
    cv2.line(img, (0, nose[1]), (1280, nose[1]), (0, 255, 255), 1)

    cv2.line(img, l_m, l_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, r_m, r_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, l_m, l_m_sym_y, (0, 255, 255), 1)
    cv2.line(img, r_m, r_m_sym_y, (0, 255, 255), 1)

    return img


def eye_avg_ratio(left_eye, right_eye):
    dist1 = dist(left_eye[0][5], left_eye[0][1])
    dist2 = dist(left_eye[0][4], left_eye[0][2])
    dist3 = dist(left_eye[0][3], left_eye[0][0])
    dist4 = dist(right_eye[0][5], right_eye[0][1])
    dist5 = dist(right_eye[0][4], right_eye[0][2])
    dist6 = dist(right_eye[0][3], right_eye[0][0])
    left_eye_ratio = (dist1+dist2)/dist3
    right_eye_ratio = (dist4+dist5)/dist6
    avg_ratio = (left_eye_ratio+right_eye_ratio)/2
    return avg_ratio


def put_text(img, text_fps, text_ear, text_es, text_blink, text_blink_avg, text_head_pose_y):
    cv2.putText(img, text_fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, text_ear, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, text_es, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, text_blink, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, text_blink_avg, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, text_head_pose_y, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    return img

