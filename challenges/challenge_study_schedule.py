def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    study_time = 0

    for login, logoff in permanence_period:
        if not (isinstance(login, int) and isinstance(logoff, int)):
            return None
        if login <= target_time and target_time <= logoff:
            study_time += 1

    return study_time
