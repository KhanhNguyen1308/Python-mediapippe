def sleep_mode(mode, ear, blink, count):
    if mode == 1:
        count += 1
        status = 'Normal'
        if count >= 25:
            status = 'Danger'
    return status