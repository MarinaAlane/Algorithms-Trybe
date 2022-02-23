def study_schedule(permanence_period, target_time):
    students_online = 0

    for log in permanence_period:
        try:
            if log[0] <= target_time <= log[1]:
                students_online += 1
        except TypeError:
            return None
    return students_online
