def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # print('=============================>', permanence_period,
    #       '||||||||||||||||||||||||||||||', target_time,
    #       '<====================================')
    students = 0
    try:
        for entrie, exite in permanence_period:
            if entrie <= target_time <= exite:
                students += 1
        return students
    except TypeError:
        return None


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))