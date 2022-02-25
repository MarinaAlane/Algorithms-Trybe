def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    counter = 0
    for login, logout in permanence_period:
        if (login <= target_time <= logout):
            counter += 1
    return counter