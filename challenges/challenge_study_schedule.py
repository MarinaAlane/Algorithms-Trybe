def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        while(permanence_period):
            contador = [item for item in permanence_period if item[0] <= target_time and item[1] >= target_time]
            return len(contador)
    except TypeError:
        return None
