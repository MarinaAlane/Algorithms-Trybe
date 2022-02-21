def study_schedule(permanence_period, target_time):
    cont = 0
    try:
        for p1, p2 in permanence_period:
            if p1 <= target_time <= p2:
                cont += 1
        return cont
    except TypeError:
        return None
