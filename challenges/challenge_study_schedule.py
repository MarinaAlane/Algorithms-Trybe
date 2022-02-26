def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    periods = []
    if type(target_time) is not int:
        return None
    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                periods.append(period)
        except TypeError:
            return None
    return len(periods)
        

