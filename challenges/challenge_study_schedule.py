def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    # Como validar um tipo no Python:
    # https://www.delftstack.com/pt/howto/python/python-check-variable-type/

    for entranceTime, exitTime in permanence_period:
        if not isinstance(entranceTime, int) or not isinstance(exitTime, int):
            return None
        if (entranceTime <= target_time <= exitTime):
            counter += 1

    return counter
