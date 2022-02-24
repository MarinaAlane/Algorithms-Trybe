def study_schedule(permanence_period, target_time):
    # 1.3
    if not target_time:
        return None

    amount = 0
    for first, last in permanence_period:
        # 1.2
        if (type(first) is not int or type(last) is not int):
            return None

        # 1.1
        if first <= target_time <= last:
            amount += 1

    return amount
