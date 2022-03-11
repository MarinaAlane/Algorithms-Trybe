def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time:
        return None

    for (item1, item2) in permanence_period:
        if type(item1) is not int or type(item2) is not int:
            return None
        if item1 <= target_time <= item2:
            count += 1

    return count
