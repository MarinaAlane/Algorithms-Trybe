def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for start, finnish in permanence_period:
        if not isinstance(start, int) or not isinstance(finnish, int):
            return None

        permanece = range(start, finnish + 1)
        if target_time in permanece:
            count += 1

    return count
