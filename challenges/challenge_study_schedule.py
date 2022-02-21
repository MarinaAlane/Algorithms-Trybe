def study_schedule(permanence_period, target_time):
    total = 0

    for student in permanence_period:
        if not target_time and target_time != 0:
            return None
        for i in range(student[0], student[1] + 1):
            if student[0] or student[1] is not int:
                return None
            if i == target_time:
                total += 1
                break
    return total
