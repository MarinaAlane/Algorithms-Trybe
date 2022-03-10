def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for index in permanence_period:
        if type(index[0]) != int or type(index[1]) != int:
            return None

        if index[0] <= target_time <= index[1]:
            count = count + 1

    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 1

study_schedule(permanence_period, target_time)
