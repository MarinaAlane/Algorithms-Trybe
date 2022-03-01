# referencias
# https://github.com/tryber/sd-011-project-algorithms/pull/98

def study_schedule(permanence_period, target_time):
    students = 0
    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                students += 1
        except TypeError:
            return None
    return students
