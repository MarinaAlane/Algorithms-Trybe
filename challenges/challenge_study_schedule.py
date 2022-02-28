def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    student = 0
    try:
        for student_entry in permanence_period:
            if student_entry[0] <= target_time <= student_entry[1]:
                student += 1
    except:
        return None
    return student