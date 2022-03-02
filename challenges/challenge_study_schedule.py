def study_schedule(permanence_period, target_time):
    try:
        students_per_period = 0
        for period in permanence_period:
            (entry_time, exit_time) = period
            if entry_time <= target_time <= exit_time:
                students_per_period += 1
        return students_per_period
    except ValueError:
        return None
