def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    contador = 0

    for entrada, saida in permanence_period:
        if type(entrada) is not int or type(saida) is not int:
            return None
        if entrada <= target_time <= saida:
            contador += 1
    return contador
