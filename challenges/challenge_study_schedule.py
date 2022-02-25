def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        counter = 0
        if not target_time:
            return None
        for item in permanence_period:
            if item[0] <= target_time and target_time <= item[1]:
                counter += 1
        return counter
    except Exception:
        None
