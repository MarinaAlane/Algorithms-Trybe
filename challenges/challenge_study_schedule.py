def study_schedule(permanence_period, target_time):
    period = permanence_period
    time = target_time
    try:
        start = 0
        for stdn in period:
            start = start+1 if stdn[0] <= time and stdn[1] >= time else start
    except TypeError:
        return start
