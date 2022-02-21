students_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

def study_schedule(permanence_period, target_time):
    total = 0

    if not target_time and target_time != 0:
        return None

    for item in permanence_period:
        for i in item:
            if type(i) is not int:
                return None

    for student in permanence_period:
        for i in range(student[0], student[1]+1):
            if i == target_time:
                total += 1
                break
    return total

print(study_schedule(students_period, 0))
