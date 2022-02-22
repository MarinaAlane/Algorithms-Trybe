def study_schedule(permanence_period, target_time):
    counter = 0

    try:
        for number in permanence_period:
            if number[0] <= target_time <= number[1]:
                counter += 1
    except TypeError:
        pass
    else:
        return counter
