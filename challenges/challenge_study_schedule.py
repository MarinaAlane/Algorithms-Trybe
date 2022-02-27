def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    online_students = 0

    for student_period in permanence_period:
        if not isinstance(student_period[0], int) or not isinstance(
            student_period[1], int
        ):
            return None

        elif student_period[0] <= target_time <= student_period[1]:
            online_students += 1

    return online_students
