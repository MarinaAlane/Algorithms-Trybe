def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        numCounter = 0
        for firstPeriod, secondPeriod in permanence_period:
            if firstPeriod <= target_time <= secondPeriod:
                numCounter += 1
        return numCounter
    except TypeError:
        return None