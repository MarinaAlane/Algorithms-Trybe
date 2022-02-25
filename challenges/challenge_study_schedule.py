def study_schedule(permanence_period, target_time):
    try:
        student = 0
        for start, stop in permanence_period:
            if start <= target_time <= stop:
                student += 1

        return student
    except TypeError:
        return None
