def study_schedule(permanence_period, target_time):
    # Cada tupla é um estudante com (horario de entrada, horario de saida)
    # counter armazena quando o estudante está online.
    counter = 0

    if type(target_time) is not int:
        return None

    # if type(permanence_period) != list:
    #     return None

    # Ajuda do Issac e colega Thiago Leite no plantão de CS.
    # Se o target_time estiver value1 e value2, adiciona-se +1 ao counter.
    for value1, value2 in permanence_period:
        if type(value1) is not int or type(value2) is not int:
            return None
        if value1 <= target_time <= value2:
            counter += 1

    return counter
