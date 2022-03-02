def study_schedule(permanence_period, target_time):
    try:
        if target_time is None:
            return None
        return studyTime(permanence_period, target_time)
    except TypeError:
        return None


def studyTime(permanence_period, target_time):
    count = 0
    for entrance, exit in permanence_period:
        if entrance <= target_time <= exit:
            count += 1
    return count
