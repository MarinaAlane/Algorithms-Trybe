def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for student in permanence_period:
            count = count+1 if student[0] <= target_time and student[1] >= target_time else count
    except TypeError:
        return count
