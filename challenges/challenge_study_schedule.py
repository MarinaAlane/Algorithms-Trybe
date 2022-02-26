def study_schedule(permanence_period, target_time):
  if not target_time:
        return None
  for start, end in permanence_period:
    if type(start) is not int or type(end) is not int:
            return None
  return True


""" 1.1 - Retorne, para uma entrada específica, a quantidade de estudantes presentes

1.2 - Retorne None se em permanence_period houver alguma entrada inválida
ok
1.3 - Retorne None se target_time recebe um valor vazio
ok
1.4 - A função poderá, em menos que 0.02s, ser executada 10.000 vezes para uma entrada pequena (tempo da execução do avaliador no Pull Request) """