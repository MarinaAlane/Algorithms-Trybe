# na sala c => Discutindo sobre o requisito
# usar a ideia do min e max para verificar o target
# e tbm isinstance()
def study_schedule(permanence_period, target_time):
    # caso target_time for nulo => retorna None
    if not target_time:
        return None
    student = 0
    for period_0, period_1 in permanence_period:
        # vendo o tipo inteiro referente ao segundo teste:
        # permanence_periods = [(4, None), ("0", 4)]
        # permanence_periods = [("A", 9), (None, 5)]
        if not isinstance(period_0, int) or not isinstance(period_1, int):
            return None
        if period_0 <= target_time <= period_1:
            student += 1
    return student


if __name__ == "__main__":
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 1))
    print(study_schedule(permanence_period, 2))
    print(study_schedule(permanence_period, 3))
    print(study_schedule(permanence_period, 4))
    print(study_schedule(permanence_period, 5))

# Algoritmos de força bruta:
# https://www.freecodecamp.org/portuguese/news/algoritmos-de-forca-bruta-explicados/
# https://www.math.tecnico.ulisboa.pt/~ccal/python/nb06.html

# Sobre o loop for:
# como o requisito avalia a posição [0] e [1] da tupla referente ao periodo
# resolvi colocar as duas posições de variavel no 'for'
# estava dando problema no tempo ao tentar usar uma variavel e delimitar
# o indice => exemplo: period[0] | period[1]
# duas variveis em loop for:
# https://stackoverflow.com/questions/51933830/using-multiple-variables-in-a-for-loop-in-python

# Usei o isinstance() pois ao usar o type não deu muito certo no quesito tempo
# https://stackoverflow.com/questions/21894575/isinstancefoo-bar-vs-typefoo-is-bar
# https://www.programiz.com/python-programming/methods/built-in/isinstance
# https://pynative.com/python-isinstance-explained-with-examples/
