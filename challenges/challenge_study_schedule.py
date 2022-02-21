def study_schedule(permanence_period, target_time):
    try:
        validate_target_time(target_time)
        count = 0

        for student_time in permanence_period:
            (entry, leave) = get_student_int_entry(student_time)
            if entry <= target_time <= leave:
                count += 1

        return count
    except TypeError:
        return None


def validate_target_time(target_time):
    if target_time is None:
        raise TypeError()


def get_student_int_entry(student_entry):
    try:
        (entry, leave) = student_entry
        return (int(entry), int(leave))
    except (TypeError, ValueError):
        raise TypeError()
