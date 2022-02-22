def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time:
        return None
    result = 0
    for enter, exit in permanence_period:
        try:
            if target_time >= enter and target_time <= exit:
                result = result + 1
        except TypeError:
            return None
    return result
# teste = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(teste, 4))