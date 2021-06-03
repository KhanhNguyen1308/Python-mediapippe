import numpy as np
from function import dist, mid_point


def head_pose_ratio(nose, left_eye, right_eye):
    try:
        l_m = mid_point(left_eye[0][0], left_eye[0][3])
        r_m = mid_point(right_eye[0][0], right_eye[0][3])
        l_m_sym_x = (l_m[0], nose[1])
        r_m_sym_x = (r_m[0], nose[1])
        l_m_sym_y = (nose[0], l_m[1])
        r_m_sym_y = (nose[0], r_m[1])
        dist_l_x = dist(l_m, l_m_sym_x)
        dist_r_x = dist(r_m, r_m_sym_x)
        dist_l_y = dist(l_m, l_m_sym_y)
        dist_r_y = dist(r_m, r_m_sym_y)
        x1 = dist_r_y/dist_l_y
        x2 = dist_r_x/dist_l_x
        x3 = dist_l_y/dist_l_x
        x4 = dist_r_y/dist_r_x
    except:
        l_m = mid_point(left_eye[0][0], left_eye[0][3])
        r_m = mid_point(right_eye[0][0], right_eye[0][3])
        l_m_sym_x = (l_m[0], nose[1])
        r_m_sym_x = (r_m[0], nose[1])
        l_m_sym_y = (nose[0], l_m[1])
        r_m_sym_y = (nose[0], r_m[1])
        dist_l_x = dist(l_m, l_m_sym_x)
        dist_r_x = dist(r_m, r_m_sym_x)
        dist_l_y = dist(l_m, l_m_sym_y)
        dist_r_y = dist(r_m, r_m_sym_y)
        x1 = 0
        x2 = dist_r_x/dist_l_x
        x3 = dist_l_y/dist_l_x
        x4 = dist_r_y/dist_r_x 
    return x1, x2, x3, x4
