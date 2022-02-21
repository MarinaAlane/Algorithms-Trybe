def study_schedule(permanence_period, target_time):
    quantity = 0
    if not target_time:
        return None
    for start, end in permanence_period:
        if (
            not start
            or not end
            or type(start) != int
            or type(end) != int
        ):
            return None
        if(start <= target_time <= end):
            quantity += 1
    return quantity
