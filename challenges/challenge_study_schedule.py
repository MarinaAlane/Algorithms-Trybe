"""
Nos arrays temos 6 estudantes

estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5 -> saída: 3, pois a quarta, a quinta e a sexta pessoa
                   estudante ainda estavam estudando nesse horário.

target_time = 4 -> saída: 3, pois a quinta e a sexta pessoa estudante
                   começaram a estudar nesse horário e a quarta ainda estavam
                   estudando.

target_time = 3 -> saída: 2, pois a terceira e a quarta pessoa estudante
                   ainda estavam estudando nesse horário.

target_time = 2 -> saída: 4, pois a primeira, a segunda, a terceira e a quarta
                   pessoa estudante estavam estudando nesse horário.

target_time = 1 -> saída: 2, pois a segunda e a quarta pessoa estudante estavam
                   estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`,
julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4
estudantes estavam presentes nesse horário!
"""


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for index in permanence_period:
        if type(index[0]) != int or type(index[1]) != int:
            # verifica que as entradas das duas posições sao numeros
            return None

        if index[0] <= target_time and index[1] >= target_time:
            # Verifica que se a primeiro valor e menor ou igual ao paramentro
            # e se o segundo valor é menor ou igual ao paramentro caso sejam
            # ambas verdade adiciona mais um ao contador
            counter = counter + 1
    return counter
