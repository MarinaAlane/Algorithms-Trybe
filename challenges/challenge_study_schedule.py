


def study_schedule(permanence_period, target_time):
    count_target_time = 0
    result = 0
    if type(target_time) != int:
        return None
    for tupla in permanence_period:
        if type(tupla[0]) != int or type(tupla[1]) != int: 
            return None
    while target_time >= count_target_time:
        count = 0
        for tupla in permanence_period:
            if tupla[0] <= target_time and tupla[1] >= target_time:
                count = count + 1
        if result < count:
            result = count
        count_target_time = count_target_time + 1
    return result


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))