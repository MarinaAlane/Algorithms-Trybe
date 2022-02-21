def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for entrada, saida in permanence_period:
            if entrada <= target_time <= saida:
                counter += 1
    except TypeError:
        return None

    return counter
