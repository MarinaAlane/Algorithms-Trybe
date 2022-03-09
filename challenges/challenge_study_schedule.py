def study_schedule(permanence_period, target_time):
    students_qtd = 0

    try:
        for time in permanence_period:
            if time[0] <= target_time <= time[1]:
                students_qtd += 1
        return students_qtd
    except TypeError:
        return None
