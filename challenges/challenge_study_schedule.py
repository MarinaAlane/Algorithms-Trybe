def study_schedule(permanence_period, target_time):
    frequency = 0
    try:
        for item in permanence_period:
            check_in = item[0]
            check_out = item[1]
            if check_in <= target_time and target_time <= check_out:
                frequency += 1
        return frequency
    except TypeError:
        return None
