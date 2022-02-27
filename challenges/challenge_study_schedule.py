def study_schedule(permanence_period, target_time):
    result = 0
    if not permanence_period:
        return None
    if not target_time:
        return None
    for item in permanence_period:
        (entry_time, exit_time) = item
        if type(entry_time) != int or type(exit_time) != int:
            return None
        if target_time >= entry_time and target_time <= exit_time:
            result += 1
    return result
