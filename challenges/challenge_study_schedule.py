def study_schedule(permanence_period, target_time):
    number_of_students = 0

    if not target_time:
        return None

    for clockIn, clockOut in permanence_period:
        if type(clockIn) is not int or type(clockOut) is not int:
            return None

        if clockIn <= target_time <= clockOut:
            number_of_students += 1

    return number_of_students
