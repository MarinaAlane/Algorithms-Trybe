def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for key, value in permanence_period:
        if type(key) != int or type(value) != int:
            return None

        if key <= target_time <= value:
            count = count + 1

    return count
