import numpy as np
import math
from function import dist, mid_point


def head_pose_ratio(nose, left_eye, right_eye):
    l_m = mid_point(left_eye[0][0], left_eye[0][3])
    r_m = mid_point(right_eye[0][0], right_eye[0][3])
    l_m_sym_x = (l_m[0], nose[1])
    r_m_sym_x = (r_m[0], nose[1])
    l_m_sym_y = (nose[0], l_m[1])
    r_m_sym_y = (nose[0], r_m[1])
    dist_l_x = dist(l_m, l_m_sym_x)
    if dist_l_x == 0:
        dist_l_x = 1
    dist_r_x = dist(r_m, r_m_sym_x)
    if dist_r_x == 0:
        dist_l_x = 1
    dist_l_y = dist(l_m, l_m_sym_y)
    if dist_l_y == 0:
        dist_l_y = 1
    dist_r_y = dist(r_m, r_m_sym_y)
    if dist_r_y == 0:
        dist_l_y = 1
    x1 = dist_r_y/dist_l_y
    x2 = dist_r_x/dist_l_x
    x3 = dist_l_y/dist_l_x
    x4 = dist_r_y/dist_r_x
    n = (r_m[1] - nose [1] )/(r_m[0] - nose [0])
    m = (l_m[1] - nose [1] )/(l_m[0] - nose [0])
    x5 = int(math.degrees(math.atan(n)))
    x6 = int(math.degrees(math.atan(m)))*(-1)
    return x1, x2, x3, x4, x5, x6
