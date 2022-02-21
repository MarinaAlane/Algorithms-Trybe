def study_schedule(permanence_period, target_time):
    total = 0

    if type(target_time) is not int:
        return None

    for valor1, valor2 in permanence_period:
        if type(valor1) is not int or type(valor2) is not int:
            return None
        if valor1 <= target_time <= valor2:
            total += 1

    return total
