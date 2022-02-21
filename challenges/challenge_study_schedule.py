import timeit


def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    try:
        for user in permanence_period:
            time_1, time_0 = user[1], user[0]
            if (time_0 <= target_time <= time_1):
                counter += 1
        return counter
    except TypeError:
        return None


if __name__ == '__main__':
    users_list = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    setup_import = (
        "from challenges.challenge_study_schedule "
        "import study_schedule"
    )
    time = timeit.timeit(
        f'study_schedule({users_list}, 2)',
        setup=f"{setup_import}",
        number=1000,
    )
    print(time)
