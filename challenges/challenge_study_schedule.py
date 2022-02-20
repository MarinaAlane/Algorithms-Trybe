def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for initial, final in permanence_period:
        if not isinstance(initial, int) or not isinstance(final, int):
            return None
        if initial <= target_time <= final:
            count += 1
    return count
