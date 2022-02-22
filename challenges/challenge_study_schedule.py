def study_schedule(permanence_period, target_time):
    student_count = 0
    try:
        for schedule in permanence_period:
            if schedule[0] <= target_time <= schedule[1]:
                student_count += 1
        return student_count
    except TypeError:
        return None
