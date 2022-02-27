def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for i in range(len(permanence_period)):
        if not isinstance(permanence_period[i][0], int) or not isinstance(
            permanence_period[i][1], int
        ):
            return None
        if permanence_period[i][0] <= target_time <= permanence_period[i][1]:
            counter += 1
    return counter
