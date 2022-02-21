def check_study_schedule(target_time):
    if type(target_time) != int:
        return None
    return True


def better_time_schedule(permanence_period, target_time):
    count = 0
    for tupla in permanence_period:
        if type(tupla[0]) != int or type(tupla[1]) != int:
            return None
        if tupla[0] <= target_time and tupla[1] >= target_time:
            count = count + 1
    return count


def study_schedule(permanence_period, target_time):
    if not check_study_schedule(target_time):
        return None
    return better_time_schedule(permanence_period, target_time)

