def study_schedule(permanence_period, target_time):
    ocurrences = 0
    for per in permanence_period:
        if type(per[0]) != int or type(per[1]) != int:
            return None

        if target_time is not None \
            and target_time >= \
                per[0] and target_time <= per[1]:
            ocurrences += 1

    if ocurrences > 0:
        return ocurrences

    return None


# teste = study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5)
# print(teste)
