def study_schedule(permanence_period, target_time):
    #            tupla: start | end
    students_presents = 0

    if not target_time:
        return None
    for start, end in permanence_period:
        if type(start) is not int or type(end) is not int:
            return None
        if start <= target_time <= end:
            # se o horario de entrada é menor que o horario especifico,
            # e este é menor que o horario de saida, entao estava presente
            students_presents += 1

    return students_presents
