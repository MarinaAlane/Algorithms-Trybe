def study_schedule(permanence_period, target_time):
    contador = 0
    try:
        for time in permanence_period:
            if target_time >= time[0] and target_time <= time[1]:
                contador += 1
    except TypeError:
        return None

    return contador


# https://stackoverflow.com/questions/48343387/valueerror-and-typeerror-in-python
