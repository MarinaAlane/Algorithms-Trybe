def study_schedule(permanence_period, target_time):
    number_of_students_online = 0

    if not target_time:
        return None

    for log_in, log_out in permanence_period:
        if type(log_in) is not int or type(log_out) is not int:
            return None

        if log_in <= target_time <= log_out:
            number_of_students_online += 1

    return number_of_students_online
