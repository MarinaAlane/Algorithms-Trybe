def study_schedule(permanence_period, target_time):
    studants_count = 0

    if type(target_time) != int:
        return None

    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None

        if target_time >= period[0] and target_time <= period[1]:
            studants_count += 1

    return studants_count
