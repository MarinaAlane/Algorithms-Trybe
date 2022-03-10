def study_schedule(permanence_period, target_time):
    total_of_students_at_target_time = 0
    for student_start_time in permanence_period:
        try:
            is_online = student_start_time[0] <= target_time <= student_start_time[1]
            if is_online:
                total_of_students_at_target_time += 1
        except TypeError:
                return None
    return total_of_students_at_target_time