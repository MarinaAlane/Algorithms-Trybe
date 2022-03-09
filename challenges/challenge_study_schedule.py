def study_schedule(permanence_period, target_time):
    # https://www.guru99.com/type-isinstance-python.html
    result = 0

    if not target_time:
        return None

    for start_time, exit_time in permanence_period:
        if type(start_time) is not int or type(exit_time) is not int:
            return None

        if start_time <= target_time <= exit_time:
            result = result + 1

    return result
