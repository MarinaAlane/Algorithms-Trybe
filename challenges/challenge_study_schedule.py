def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    contador = 0
    for p1, p2 in permanence_period:
        if (
            type(p1) != int or p1 is None or type(
                p2) != int or p2 is None
        ):
            return None
        if p1 <= target_time <= p2:
            contador += 1
    return contador
