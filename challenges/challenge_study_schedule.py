def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for student in permanence_period:
        if student[0] <= target_time <= student[1]:
            count += 1
    return count
