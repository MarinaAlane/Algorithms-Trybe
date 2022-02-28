def study_schedule(permanence_period, target_time):
    contador = 0
    try:
        for entry_exit in permanence_period:
            if entry_exit[0] <= target_time <= entry_exit[1]:
                contador += 1
    except TypeError:
        return None
    else:
        return contador
