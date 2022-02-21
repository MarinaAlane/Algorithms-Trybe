def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    best_time_count = 0
    for student_time in permanence_period:
        if type(student_time[0]) != int or type(student_time[1]) != int:
            return None
        if student_time[0] <= target_time <= student_time[1]:
            best_time_count += 1

    return best_time_count
