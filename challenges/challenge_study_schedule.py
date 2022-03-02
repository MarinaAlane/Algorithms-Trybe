def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    time = 0
    for num, value in permanence_period:

        if type(num) != int or type(value) != int:
            return None

        if num <= target_time <= value:
            time += 1

    return time
