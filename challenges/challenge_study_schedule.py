def study_schedule(permanence_period, target_time):
    students_online = 0
    try:
        for enter_time, exit_time in permanence_period:
            if exit_time >= target_time >= enter_time:
                students_online += 1
    except TypeError:
        return None
    return students_online
