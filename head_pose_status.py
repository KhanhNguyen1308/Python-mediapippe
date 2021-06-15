def head_pose_status(x1, x2):
    try:
        if x1 >= 0.2 and x1 <= 0.5:
            if x2 >= 0.7 and x2 <= 1.4:
                pose_status = "Straight"
        elif x1 < 0.2 or False:
            if x2 >= 0.7 and x2 <= 1.4:
                pose_status = "Straight leaning to the Right"
        elif x1 > 0.5:
            if x2 >= 0.7 and x2 <= 1.4:
                pose_status = "Straight leaning to the Left"
    except:
        pose_status = 'None Face'
    return pose_status


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


