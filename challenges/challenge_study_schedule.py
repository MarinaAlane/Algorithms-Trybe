def study_schedule(permanence_period, target_time):
    total = 0
    if not target_time and target_time != 0:
        return None
    try:
        for student in permanence_period:
            for i in range(student[0], student[1] + 1):
                if i == target_time:
                    total += 1
                    break
    except TypeError:
        return None

    return total
