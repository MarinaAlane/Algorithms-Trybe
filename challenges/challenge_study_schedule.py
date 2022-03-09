def study_schedule(permanence_period, target_time):
    students_count = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                students_count += 1
        return students_count
    except TypeError:
        return None
