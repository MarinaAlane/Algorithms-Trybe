# função para descobrir qual o melhor horário para disponibilizar os conteúdos
# o que retornar o maior contador será o horário selecionado
# permanence_period @{Array}  - horário de entrada e saída de cada aluno (lista de tuplas)
# target_time       @{Number} - horário alvo
def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
        return counter
    except TypeError:
        return None
