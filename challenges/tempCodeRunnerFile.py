def study_schedule(permanence_period, target_time):
    return [
        number
        for number in permanence_period
        if target_time in range(number[0], number[1]) or target_time in number
    ]


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


print(study_schedule(permanence_period, 5))
