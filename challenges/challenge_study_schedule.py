def study_schedule(permanence_period, target_time):
    numberOfStudentsPresent = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time and period[1] >= target_time:
                numberOfStudentsPresent += 1
        return numberOfStudentsPresent
    except TypeError:
        return None
    else:
        return numberOfStudentsPresent
