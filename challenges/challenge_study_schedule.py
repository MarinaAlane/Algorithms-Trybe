def study_schedule(permanence_period, target_time):
    count = 0
    for period1, period2 in permanence_period:
        if (type(period1) is  int) and (type(period2) is  int) and (type(target_time) is int):
            if target_time >= period1 and target_time<= period2:
                count += 1
        else:
            return None
    return count

print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)],3))

print()