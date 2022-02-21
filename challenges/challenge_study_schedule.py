def study_schedule(permanence_period, target_time):
    quantity = 0
    for period in permanence_period:
        start, end = period
        if None in period or type(start) != int or type(end) != int or target_time == None:
            return None
        if(start <= target_time <= end):
            quantity += 1
    return quantity