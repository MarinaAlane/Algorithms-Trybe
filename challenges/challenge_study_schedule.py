def verify_none(target_time):
    if target_time is None:
        return None


def study_schedule(permanence_period, target_time):
    result = 0
    verify_none(target_time)
    for studant in permanence_period:
        try:
            if studant[0] <= target_time <= studant[1]:
                result = result + 1
        except TypeError:
            return None
    return result
