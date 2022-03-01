def study_schedule(permanence_period, target_time):
    students_counter = 0
    try:
        # p aqui é uma tupla de horários, sendo (entrada, saída)
        for p in permanence_period:
            if p[0] <= target_time <= p[1]:
                students_counter += 1
    # aqui o TypeError é pra caso o algum valor seja nulo
    # https://www.pylenin.com/blogs/type-error-exception/
    except TypeError:
        return None
    else:
        return students_counter
