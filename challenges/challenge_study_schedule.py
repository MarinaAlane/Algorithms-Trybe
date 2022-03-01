def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for tuple_data in permanence_period:
            if tuple_data[0] <= target_time <= tuple_data[1]:
                counter += 1
        return counter
    except TypeError:
        return None
