def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    contador = 0
    for p in permanence_period:
        if (type(p[0]) != int or p[0] is None or type(p[0]) != int or p[1] is None):
            return None
        if target_time >= p[0] and target_time <= p[1]:
            contador += 1
    return contador
