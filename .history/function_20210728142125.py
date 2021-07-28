import cv2
import numpy as np


def list2point(list):
    point = (list[0], list[1])
    return point


def mid_point(p1, p2):
    mp = (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    return mp


def dist(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a-b)


def draw_point(img, nose_list, left_eye_list, right_eye_list, mount_list):
    left_eye0 = list2point(left_eye_list[0][0])
    left_eye1 = list2point(left_eye_list[0][1])
    left_eye2 = list2point(left_eye_list[0][2])
    left_eye3 = list2point(left_eye_list[0][3])
    left_eye4 = list2point(left_eye_list[0][4])
    left_eye5 = list2point(left_eye_list[0][5])

    right_eye0 = list2point(right_eye_list[0][0])
    right_eye1 = list2point(right_eye_list[0][1])
    right_eye2 = list2point(right_eye_list[0][2])
    right_eye3 = list2point(right_eye_list[0][3])
    right_eye4 = list2point(right_eye_list[0][4])
    right_eye5 = list2point(right_eye_list[0][5])

    mount0 = list2point(mount_list[0][0])
    mount1 = list2point(mount_list[0][1])
    mount2 = list2point(mount_list[0][2])
    mount3 = list2point(mount_list[0][3])
    mount4 = list2point(mount_list[0][4])
    mount5 = list2point(mount_list[0][5])
    mount6 = list2point(mount_list[0][6])
    mount7 = list2point(mount_list[0][7])

    nose = list2point(nose_list)

    l_m = mid_point(left_eye0, left_eye3)
    r_m = mid_point(right_eye0, right_eye3)

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
    cv2.circle(img, left_eye0, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye1, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye2, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye3, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye4, 1, (0, 255, 0), 1)
    cv2.circle(img, left_eye5, 1, (0, 255, 0), 1)

    cv2.circle(img, right_eye0, 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye1, 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye2, 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye3, 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye4, 1, (0, 255, 0), 1)
    cv2.circle(img, right_eye5, 1, (0, 255, 0), 1)

    cv2.circle(img, mount0, 1, (0, 255, 0), 1)
    cv2.circle(img, mount1, 1, (0, 255, 0), 1)
    cv2.circle(img, mount2, 1, (0, 255, 0), 1)
    cv2.circle(img, mount3, 1, (0, 255, 0), 1)
    cv2.circle(img, mount4, 1, (0, 255, 0), 1)
    cv2.circle(img, mount5, 1, (0, 255, 0), 1)
    cv2.circle(img, mount6, 1, (0, 255, 0), 1)
    cv2.circle(img, mount7, 1, (0, 255, 0), 1)

    cv2.line(img, nose, l_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, nose, r_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, nose, l_m_sym_y, (0, 255, 255), 1)
    cv2.line(img, nose, r_m_sym_y, (0, 255, 255), 1)

    cv2.line(img, l_m, l_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, r_m, r_m_sym_x, (0, 255, 255), 1)
    cv2.line(img, l_m, l_m_sym_y, (0, 255, 255), 1)
    cv2.line(img, r_m, r_m_sym_y, (0, 255, 255), 1)

    cv2.line(img, mount0, mount4, (0, 255, 255), 1)
    cv2.line(img, mount1, mount7, (0, 255, 255), 1)
    cv2.line(img, mount2, mount6, (0, 255, 255), 1)
    cv2.line(img, mount3, mount5, (0, 255, 255), 1)

    return img


def eye_avg_ratio(left_eye_list, right_eye_list):
    left_eye0 = list2point(left_eye_list[0][0])
    left_eye1 = list2point(left_eye_list[0][1])
    left_eye2 = list2point(left_eye_list[0][2])
    left_eye3 = list2point(left_eye_list[0][3])
    left_eye4 = list2point(left_eye_list[0][4])
    left_eye5 = list2point(left_eye_list[0][5])

    right_eye0 = list2point(right_eye_list[0][0])
    right_eye1 = list2point(right_eye_list[0][1])
    right_eye2 = list2point(right_eye_list[0][2])
    right_eye3 = list2point(right_eye_list[0][3])
    right_eye4 = list2point(right_eye_list[0][4])
    right_eye5 = list2point(right_eye_list[0][5])

    dist1 = dist(left_eye5, left_eye1)
    dist2 = dist(left_eye4, left_eye2)
    dist3 = dist(left_eye3, left_eye0)
    dist4 = dist(right_eye5, right_eye1)
    dist5 = dist(right_eye4, right_eye2)
    dist6 = dist(right_eye3, right_eye0)
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

def head_pose(results_pose, img, pose_xy):
    for pose_lms in results_pose.pose_landmarks:
                for lm in pose_lms.landmark:
                    ih, iw = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    pose_xy.append([x, y])


def predict(X, model):
    y = model.predict(X)
    return int(y)