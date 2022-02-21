def study_schedule(permanence_period, target_time):
    try:
        if target_time is None:
            return
        return count_study_time(permanence_period, target_time)
    except TypeError:
        return


def count_study_time(permanence_period, target_time):
    count = 0
    for entrance, exit in permanence_period:
        for item in range(entrance, exit + 1):
            if target_time == item:
                count += 1
    return count

# def count_study_time(permanence_period, target_time):
#     return len([1 for entrance, exit in permanence_period
#                 for item in range(entrance, exit + 1)
#                 if target_time == item])
