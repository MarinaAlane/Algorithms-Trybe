def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students = 0
    try:
        for start, end in permanence_period:
            if start <= target_time <= end:
                students += 1
        return students
    except TypeError:
        return None
