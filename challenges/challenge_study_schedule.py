def study_schedule(permanence_period, target_time):
    try:
        students_counter = 0
        for student_period in permanence_period:
            if student_period[0] <= target_time <= student_period[1]:
                students_counter += 1
        return students_counter
    except TypeError:
        return None

# a função study_schedule recebe como parametro a lista de tuplas de horários
# de entrada e saida de cada estudadnte no site de ensino.
# o segundo parametro é o target_time que é o horário desejado, ou seja, o
# próprio usuário envia o horário ao qual ele quer saber o numero de usuarios
# naquela determinada hora. Primeiro questiono se o target time está vazio ou
# não e se estiver vazio retorna None. Faço um try/except e inicio um contador
# de numero de estudantes para o target time desejado faço um for para iterar
# na lista de permanence_period e faço um if verificando se o target_time está
# entre o primeiro e o segundo itnes de cada uma das tuplas. OBS: para acessar
# a os itens da tupla posso fazer o acesso como se fosse uma lista e usar []
# no elemento desejado. Se o target_time estiver dentro do range da tupla,
# entao acrescenta um digito ao contador de estudantes. Se algo der errado
# retorno None
# tive que tirar a parte de verificar se o parametro foi passado ou não para
# tirar a complexidade da função.
