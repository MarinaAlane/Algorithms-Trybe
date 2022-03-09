def study_schedule(permanence_period, target_time):
    if not (
        target_time
        and isinstance(permanence_period, list)
      ):
        return None

    students = 0

    for (start, end) in permanence_period:

        if not (isinstance(start, int) and isinstance(end, int)):
            return None

        if target_time >= start and target_time <= end:
            students += 1

    return students
