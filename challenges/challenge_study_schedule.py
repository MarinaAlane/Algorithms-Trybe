def study_schedule(permanence_period, target_time):
    count_time = 0
    try:
        for study_time in permanence_period:
            check_in_time = study_time[0]
            check_out_time = study_time[1]
            if check_in_time <= target_time <= check_out_time:
                count_time += 1
        return count_time

    except TypeError:
        return None
