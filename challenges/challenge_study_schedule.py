def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None

    count = 0

    for tuple in permanence_period:
        # https://pt.stackoverflow.com/questions/341085/como-validar-se-um-valor-%C3%A9-uma-tupla-possuindo-uma-string-e-um-inteiro
        if not isinstance(tuple[0], int) or not isinstance(tuple[1], int):
            return None
        if tuple[0] <= target_time <= tuple[1]:
            count += 1

    return count
