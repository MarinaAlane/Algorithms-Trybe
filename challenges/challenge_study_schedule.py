def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for time in permanence_period:
        if type(time[0]) is not int or type(time[1]) is not int:
            return None
        if time[0] <= target_time and time[1] >= target_time:
            count += 1
    return count


if __name__ == '__main__':
    permanence_period_data = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    result = study_schedule(permanence_period_data, 5)
    print(result)
