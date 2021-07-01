def head_pose_status(x5, x6, x2):
    try:
        if x5 > 60:
            if x6 >= 32:
                pose_status = "Bend down"
                mode = 1
            elif x6 < 32:
                if x2 >=0.8 and x2 <= 1.3:
                    pose_status = "Straight"
                    mode = 0
                elif x2 > 1.3:
                    pose_status = "Leaning to the Left"
                    mode = 3
                elif x2 < 0.8:
                    pose_status = "x5 > 60 and x2 < 0.8"
                    mode = 9
        elif 40 <= x5 <= 60:
            if x6 >= 20 and x6 <=34:
                if x2 >=0.7 and x2 <= 1.3:
                    pose_status = "Straight"
                    mode = 0
                elif x2 < 0.7:
                    pose_status = "Ben down, leaning to the right"
                    mode = 1
                elif x2 > 1.3:
                    pose_status = "Ben down, leaning to the right"
                    mode = 1
            elif x6 > 34:
                if x2 < 0.8:
                    pose_status = "Leaning to the Right"
                    mode = 2
                elif x2 >=0.8 and x2 <= 1.3:
                    pose_status = "Bend down"
                    mode = 1
                elif x2 > 1.3:
                    pose_status = "Bend down and Look at the Left"
                    mode = 4
            elif x6 <20:
                pose_status = "40 <= x5 <= 60, x6 <20"
                mode = 9
            
        elif 20 <= x5 < 40:
            if x6 >= 50:
                pose_status = "Leaning to the Right"
                mode = 2
            elif 20 <= x6 < 50:
                pose_status = "Straight to camera"
                mode = 8
            elif x6 < 20:
                pose_status = "20 <= x5 < 40 and x6 < 20"
                mode = 9
        else:
            pose_status = "Can't detect!!"
            mode = 9
    except:
        pose_status = 'WRONG DATA'
        mode = 9
    return pose_status, mode


def eye_stat(eye_avg_ratio, count, blink, mode):
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
        eye_status = 'Error'
        blink = 0
        count = 0
    return eye_status, blink, count

 