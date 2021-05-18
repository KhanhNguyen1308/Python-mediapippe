import numpy as np


def dist(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a-b)


def mid_point(p1, p2):
    mp = (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    return mp


def head_pose_x(nose, left_eye, right_eye):
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

    ratio_r = dist_r_x / dist_r_y
    ratio_l = dist_l_x / dist_l_y

    return ratio_r, ratio_l


def head_pose_y(nose, left_eye, right_eye):
    l_m = mid_point(left_eye[0][0], left_eye[0][3])
    r_m = mid_point(right_eye[0][0], right_eye[0][3])

    l_m_sym_x = (l_m[0], nose[1])
    r_m_sym_x = (r_m[0], nose[1])

    dist_l_x = dist(l_m, l_m_sym_x)
    dist_r_x = dist(r_m, r_m_sym_x)

    y_ratio = (dist_r_x / dist_l_x)
    return y_ratio


def head_pose_z(nose, left_eye, right_eye):
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

    ratio_r = dist_r_x/dist_r_y
    ratio_l = dist_l_x/dist_l_y
    avg_ratio = (ratio_r+ratio_l)/2
    return avg_ratio
