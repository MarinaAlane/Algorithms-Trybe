def study_schedule(permanence_period, target_time):
    for e, s in permanence_period:
        c = 0
        try:
            if e <= target_time <= s:
                c += 1
            return c
        except TypeError:
            return None
