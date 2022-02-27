def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    counter = 0
    for login, logout in permanence_period:
        if type(login) is not int or type(logout) is not int:
            return None
        if (login <= target_time <= logout):
            counter += 1
    return counter
