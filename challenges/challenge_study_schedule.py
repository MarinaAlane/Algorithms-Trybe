def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for period in permanence_period:
            ta = period[0]
            tb = period[1]
            count = ta <= target_time and tb >= target_time

            if count is True:
                students += 1

        return students

    except TypeError:
        return None
