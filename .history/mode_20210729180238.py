def sleep_mode(mode, ear, blink, count):
    if mode == 1:
        if count >= 25:
            status = 'Danger'
    else:
        status = 'Normal'
    return status