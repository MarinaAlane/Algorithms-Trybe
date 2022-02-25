def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        result = [
            (i,j) for i, j in permanence_period if i <= target_time and target_time <= j
            ]
        return len(result)
    except TypeError:
        return None
