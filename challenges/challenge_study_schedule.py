def study_schedule(permanence_period, target_time):
    curr_students = 0
    for i in range(0, len(permanence_period)):
        try:
            if (
                permanence_period[i][1]
                >= target_time >= permanence_period[i][0]
            ):
                curr_students += 1
        except TypeError:
            return None
    return curr_students
