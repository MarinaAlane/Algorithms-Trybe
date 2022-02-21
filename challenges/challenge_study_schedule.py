def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for tuple in permanence_period:
            if tuple[0] <= target_time <= tuple[1]:
                counter += 1
    except TypeError:
        return None
    return counter
