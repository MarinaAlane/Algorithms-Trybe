def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for (entry, leave) in permanence_period:
        if type(entry) is not int or type(leave) is not int:
            return None

        if entry <= target_time <= leave:
            counter += 1

    return counter
