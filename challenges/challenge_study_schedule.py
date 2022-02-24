def study_schedule(permanence_period, target_time):
    number_of_students = 0
    
    for clockIn, clockOut in permanence_period:
        if (type(clockIn) != int or type(clockOut) != int) or not target_time:
            return None
        
        if clockIn <= target_time <= clockOut:
            number_of_students += 1
    
    return number_of_students
