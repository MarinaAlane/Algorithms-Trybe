def study_schedule(permanence_period, target_time):
    contador = 0
    try:
        for time in permanence_period:
            if target_time >= time[0] and target_time <= time[1]:
                print(time[0], time[1])
                contador += 1
                print(contador)
    except TypeError:
        return None

    return contador


# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target_time = 4

permanence_periods = [(4, "e"), ("0", 4)]
target_time = 4

print(
    study_schedule(
        permanence_period=permanence_periods, target_time=target_time
    )
)

# https://stackoverflow.com/questions/48343387/valueerror-and-typeerror-in-python
