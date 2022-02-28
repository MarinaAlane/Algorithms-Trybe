def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for num in permanence_period:
            if num[0] <= target_time <= num[1]:
                counter += 1
    except TypeError:
        return None
    else:
        return counter
