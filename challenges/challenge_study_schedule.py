def study_schedule(permanence_period, target_time):
    #https://github.com/tryber/sd-011-project-algorithms/pull/14/files
    # Celso Oliva
    try:
        count = 0
        for tupla in permanence_period:
            count = count+1 if tupla[0] <= target_time and tupla[1] >= target_time else count
        return count
    except TypeError:
        return None
