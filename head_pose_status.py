def head_pose_x_status(ratio_l, ratio_r):
    try:
        if ratio_r >= 1.1 and ratio_l <= 0.7:
            x_status = 'leaning to the left'
        elif ratio_l >= 1.1 and ratio_r <= 0.7:
            x_status = 'leaning to the right'
        else:
            x_status = 'straight'
    except:
        x_status = 'Non Face'
    return x_status


def head_pose_y_status(head_pose_y_ratio):
    try:
        if head_pose_y_ratio >= 1.5 or head_pose_y_ratio <= 0.55:
            y_status = 'sloping'
        elif head_pose_y_ratio < 1.5 and head_pose_y_ratio > 0.55:
            y_status = 'straight'
    except:
        y_status = 'Non Face'
    return y_status


def head_pose_z_status(x_status, y_status, avg_ratio):
    try:
        if x_status == 'straight' and y_status == 'straight':
            if avg_ratio >= 1:
                z_status = 'bow'
            elif avg_ratio < 1:
                z_status = 'straight'
        elif x_status == 'leaning to the left' and y_status == 'straight':
            if avg_ratio >= 1:
                z_status = 'bow'
        elif x_status == 'leaning to the right' and y_status == 'straight':
            if avg_ratio >= 1:
                z_status = 'bow'
    except:
        z_status = 'Non Face'
    return z_status


def eye_stat(eye_avg_ratio, count, blink):
    try:
        if eye_avg_ratio <= 0.53:
            eye_status = 'Close'
            count += 1
        else:
            eye_status = 'Open'
            if count > 0:
                blink += 1
            count = 0
    except:
        eye_status = 'Non Face'
        blink = 0
        count = 0
    return eye_status, blink, count


