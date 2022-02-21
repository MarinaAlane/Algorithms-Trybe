permanence_periods = [(4, None), ("0", 4)]


def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for schedule in permanence_period:
            if schedule[0] == target_time or schedule[1] == target_time:
                counter += 1
            if schedule[0] < target_time < schedule[1]:
                counter += 1
        return counter if counter > 0 else None
    except TypeError:
        return None


# print(study_schedule(permanence_periods, 4))
