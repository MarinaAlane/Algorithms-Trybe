def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for start_time, end_time in permanence_period:
            if not target_time:
                return None
            if start_time <= target_time and target_time <= end_time:
                count += 1
        return count
    except TypeError:
        return None
