def study_schedule(permanence_period, target_time):
    try:
        rep = 0
        for start, end in permanence_period:
            if (start <= target_time <= end):
                rep += 1
    except TypeError:
        return None
    return rep
    """ Faça o código aqui. """
