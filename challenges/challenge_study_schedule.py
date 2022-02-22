
def study_schedule(permanence_period, target_time):
    count = 0
    for time in permanence_period:
        try:
            if time[0] <= target_time and target_time <= time[1]:
                count += 1
        except TypeError:
            return None
    return count
