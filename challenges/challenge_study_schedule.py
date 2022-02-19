
def study_schedule(permanence_period, target_time):
    count = 0
    for time in permanence_period:
        if (
            type(time[0]) != int
            or type(time[1]) != int
            or type(target_time) != int
        ):
            return None
        if time[0] <= target_time and target_time <= time[1]:
            count += 1
    return count
