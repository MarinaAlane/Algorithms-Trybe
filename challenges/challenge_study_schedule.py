def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        counter = 0
        for period_one, period_two in permanence_period:
            if period_one <= target_time <= period_two: counter += 1
        return counter
    except TypeError:
        return None
