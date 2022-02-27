# Usei o try except para que ele tentasse pegar uma informação, ou retornar
# um erro caso essa informação não exista.
# no if, verifiquei se o target_time está entre a primeira e a segunda
# posição informadas em cada tupla do permanence_period. Se estiver, conta
# 1 e passa pra proxima tupla, se não,ele vai pro erro.

def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
        return counter
    except TypeError:
        return None
