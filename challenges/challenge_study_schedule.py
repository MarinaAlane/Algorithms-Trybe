def study_schedule(permanence_period, target_time):

    studentsPeriod = 0
    try:
        for period in permanence_period:
            time_entered = period[0]
            time_leave = period[1]
            if target_time >= time_entered and target_time <= time_leave:
                studentsPeriod += 1
        return studentsPeriod
    except TypeError:
        return None
