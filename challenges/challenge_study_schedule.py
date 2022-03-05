def study_schedule(permanence_period, target_time):
    # if target_time is None:
    #     return None

    count = 0

    # for period in permanence_period:
    #     if not isinstance(period1, int) or not isinstance(period2, int):
    #         return None

    #     if period1 <= target_time <= period2:
    #         count = count + 1

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                count = count + 1
    except TypeError:
        return None

    return count
