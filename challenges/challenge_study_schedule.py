def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    counter = 0
    for entrada, saida in permanence_period:
        if type(entrada) is not int or type(saida) is not int:
            return None
        if entrada <= target_time <= saida:
            counter += 1
    return counter
