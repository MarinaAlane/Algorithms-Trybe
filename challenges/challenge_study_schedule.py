def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for entrada, saida in permanence_period:
            if entrada <= target_time <= saida:
                students += 1
    except TypeError:
        return None
    return students
