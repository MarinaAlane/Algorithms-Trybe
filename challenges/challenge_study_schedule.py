def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if not target_time:
        return None
    for item in permanence_period:
        if item[0] <= target_time and target_time <= item[1]:
            counter += 1
    return counter


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 3))
