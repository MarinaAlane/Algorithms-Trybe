def study_schedule(permanence_period, target_time):
    quantity = 0
    for start, end in permanence_period:
        if (not start
            or not end
            or type(start) != int
            or type(end) != int
            or target_time == None):
            return None
        if(start <= target_time <= end):
            quantity += 1
    return quantity