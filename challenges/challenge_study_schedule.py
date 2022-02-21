def counter_schedule(permanence_period, target_time):
    counter = 0
    for schedule in permanence_period:
        if schedule[0] == target_time or schedule[1] == target_time:
            counter += 1
        if schedule[0] < target_time < schedule[1]:
            counter += 1
    return counter


def study_schedule(permanence_period, target_time):
    try:
        return counter_schedule(permanence_period, target_time)
    except TypeError:
        return None
