def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    counter = 0
    for user in permanence_period:
        time_1, time_0 = user[1], user[0]
        if type(time_0) != int or type(time_1) != int:
            return None
        elif (time_0 <= target_time <= time_1):
            counter += 1
    return counter


if __name__ == '__main__':
    users_list = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(users_list, 2))
