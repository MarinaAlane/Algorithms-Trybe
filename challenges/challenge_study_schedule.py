def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for x1, x2 in permanence_period:
            if x1 <= target_time <= x2:
                counter += 1
        return counter
    except TypeError:
        return None
