def study_schedule(permanence_period, target_time):
    try:
        if target_time is None:
            return
        return count_study_time(permanence_period, target_time)
    except TypeError:
        return


def count_study_time(permanence_period, target_time):
    count = 0
    for entrance, exit in permanence_period:
        if entrance <= target_time <= exit:
            count += 1
    return count
