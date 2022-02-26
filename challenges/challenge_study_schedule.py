def study_schedule(permanence_period, target_time):
    if target_time == 0 or target_time is None:
        return None

    students_online = 0
    for student in permanence_period:
        if isinstance(student[0], int) and isinstance(student[1], int):
            if student[1] >= target_time >= student[0]:
                students_online += 1
        else:
            return None

    return students_online
