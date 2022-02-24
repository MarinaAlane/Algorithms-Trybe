def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    counter = 0

    for singleTime in permanence_period:
        if(type(singleTime[0]) is not int or type(singleTime[1]) is not int):
            return None
        if singleTime[0] <= target_time <= singleTime[1]:
            counter += 1

    return counter
