def study_schedule(permanence_period, target_time):
    count = 0

    # Comments: Verifica se target_time é valído.
    if not target_time:
        return None

    # Comments: Verifica se algum dos valores de cada tupla é uma instância do/
    # tipo inteiro. Se sim, retorna None.
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        # Comments: Verifica se o target_time está contido nos intervalos de\
        # cada tupla da lista.
        if period[0] <= target_time <= period[1]:
            count += 1

    return count
