def study_schedule(permanence_period, target_time):
    counter = 0
    for login, logout in permanence_period:
        if (login <= target_time <= logout):
            counter += 1
    return counter