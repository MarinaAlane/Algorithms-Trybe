def study_schedule(permanence_period, target_time):
    count_student = 0

    for item in permanence_period:
        try:
            if item[0] <= target_time <= item[1]:
                count_student += 1
        except TypeError:
            return None
    return count_student
