def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    time = 0
    for num, value in permanence_period:

        if type(num) != int or type(value) != int:
            return None

        if num <= target_time <= value:
            time += 1

    return time


permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_periods, 5))
