def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for index in permanence_period:
        if type(index[0]) != int or type(index[1]) != int:
            # verifica que as entradas das duas posições sao numeros
            return None

        if index[0] <= target_time and index[1] >= target_time:
            # Verifica que se a primeiro valor e menos ou igual ao paramentro
            # e se o segundo valor é menor ou igual ao paramentro
            counter = counter + 1
            # Caso seja adiciona mais um ao contador
    return counter
