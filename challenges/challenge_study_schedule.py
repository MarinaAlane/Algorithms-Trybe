def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    students_per_period = 0
    for entry_time, exit_time in permanence_period:
        if type(entry_time) is not int or type(exit_time) is not int:
            return None
        if entry_time <= target_time <= exit_time:
            students_per_period += 1
    return students_per_period
