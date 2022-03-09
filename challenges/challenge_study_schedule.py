def study_schedule(permanence_period, target_time):
    index = 0
    for e in permanence_period:
        try:
            if e[0] <= target_time <= e[1]:
                index += 1
        except TypeError:
            return None
    return index
