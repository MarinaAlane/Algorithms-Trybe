def study_schedule(permanence_period, target_time):
    """
    Caso o target_time passado seja nulo, o valor
    retornado pela função deve ser None
    """
    if not target_time:
        return None
    return toocomplex(permanence_period, target_time)


# https://www.flake8rules.com/rules/C901.html
def toocomplex(permanence_period, target_time):
    i = 0
    try:
        for values in permanence_period:
            """
            Dica: Quando vou saber qual o melhor horário?
            Quando o contador retornado pela função for o maior.
            """
            if values[0] <= target_time <= values[1]:
                i += 1
    except TypeError:
        """
        Retorne None se em permanence_period houver alguma entrada inválida
        """
        return None
    return i
