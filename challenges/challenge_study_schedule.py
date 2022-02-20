def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for student_period in permanence_period:
            student_period[0] * student_period[1]
            if student_period[0] == target_time or student_period[1] == target_time:
                counter += 1
            elif student_period[0] < target_time < student_period[1]:
                counter += 1
        return counter
    except Exception:
        return None
