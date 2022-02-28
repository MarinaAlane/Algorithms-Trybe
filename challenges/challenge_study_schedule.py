def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for entry_time, exit_time in permanence_period:
        if type(entry_time) is not int or type(exit_time) is not int:
            return None
        if entry_time <= target_time <= exit_time:
            counter += 1

    return counter
