permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 2

def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for student_period in permanence_period:
        start_hour = student_period[0]
        end_hour = student_period[1]
        if (type(start_hour) != int or type(end_hour) != int):
            return None
        if (start_hour <= target_time <= end_hour):
            counter += 1
    return counter

result = study_schedule(permanence_period, target_time)
print(result)
