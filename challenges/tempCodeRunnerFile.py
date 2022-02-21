def study_schedule(permanence_period, target_time):
    result = 0

    if not bool(target_time):
        return None

    for number in permanence_period:
        if type(number[0]) != int or type(number[0]) != int:
            return None
        elif (
            number[0] <= target_time <= number[1]
            # target_time in range(number[0], number[1]) or target_time in number
        ):
            result += 1
    return result


permanence_period = [(2, 2), (1, 2), ('a', 3), (1, 5), (4, 5), (4, 5)]


print(study_schedule(permanence_period, None))
