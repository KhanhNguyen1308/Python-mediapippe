def head_pose_status(x5, x6, x2):
    try:
        if x5 > 60:
            if x6 >= 40:
                pose_status = "Bend down"
                mode = 1
            elif x6 < 40:
                if x2 <= 1.3:
                    pose_status = "Straight"
                    mode = 0
                elif x2 > 1.3:
                    pose_status = "Leaning to the Left"
                    mode = 3
        elif 40 <= x5 <= 60:
            if x6 <= 40:
                if 0.7 <= x2 <= 1.3:
                    pose_status = "Straight"
                    mode = 0
                elif x2 < 0.7:
                    pose_status = "Ben down, leaning to the right"
                    mode = 1
                elif x2 > 1.3:
                    pose_status = "Ben down, leaning to the right"
                    mode = 1
            elif x6 > 40:
                if x2 < 0.8:
                    pose_status = "Leaning to the Right"
                    mode = 2
                elif 0.8 <= x2 <= 1.3:
                    pose_status = "Bend down"
                    mode = 1
                elif x2 > 1.3:
                    pose_status = "Bend down and Look at the Left"
                    mode = 4

        elif x5 < 40:
            if x6 >= 50:
                pose_status = "Leaning to the Right"
                mode = 2
            elif x6 < 50:
                if x2 >= 0.7:
                    pose_status = "Straight"
                    mode = 0
                else:
                    pose_status = "Leaning to the Right"
                    mode = 2

        else:
            pose_status = "Can't detect!!"
            mode = 9
    except:
        pose_status = 'WRONG DATA'
        mode = 11
    return pose_status, mode


def eye_stat(eye_avg_ratio, count, blink, mode):
    try:
        if mode == 0:
            if eye_avg_ratio <= 0.485:
                eye_status = 'Close'
                count += 1
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
        elif mode == 1:
            eye_status = ''
            count +=1
        elif mode == 2:
            if eye_avg_ratio <= 0.6:
                eye_status = 'Close'
                count += 1
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
        elif mode == 3:
            if eye_avg_ratio <= 0.53:
                eye_status = 'Close'
                count += 1
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
        elif mode == 4:
            if eye_avg_ratio <= 0.6:
                eye_status = 'Close'
                count += 1
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0

    except:
        eye_status = 'Error'
        blink = 0
        count = 0
    return eye_status, blink, count

