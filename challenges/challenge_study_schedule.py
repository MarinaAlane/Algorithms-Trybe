def study_schedule(permanence_period, target_time):
    if target_time == 0 or target_time is None:
        return None

    online_studants = 0
    for student_time in permanence_period:
        if not isinstance(student_time[0], int) or not isinstance(
            student_time[1], int
        ):
            return None
        if student_time[0] <= target_time and student_time[1] >= target_time:
            online_studants = online_studants + 1

    return online_studants
