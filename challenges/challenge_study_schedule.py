

def study_schedule(permanence_period, target_time):
    try:
        online_students = [
            True for entry, exit in permanence_period if exit >= target_time >= entry]
    except TypeError:
        return None
    return len(online_students)
