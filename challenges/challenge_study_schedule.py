def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for period in permanence_period:
            period[0] * period[1]
            if period[0] == target_time or period[1] == target_time:
                counter += 1
            elif period[0] < target_time < period[1]:
                counter += 1
        return counter
    except Exception:
        return None
