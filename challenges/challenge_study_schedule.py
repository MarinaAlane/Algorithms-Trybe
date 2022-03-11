def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for key, value in permanence_period:
            if key <= target_time <= value:
                count = count + 1
    except TypeError:
        return None

    return count
