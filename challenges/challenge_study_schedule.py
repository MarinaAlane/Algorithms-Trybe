def study_schedule(permanence_period, target_time):
    count = 0
    for enter_period, exit_period in permanence_period:
        try:
            if enter_period <= target_time <= exit_period:
                count += 1
        except TypeError:
            return None
    return count
