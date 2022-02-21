def study_schedule(period, time):
    try:
        online_students = [
            True for entry, exit in period if exit >= time >= entry]
    except TypeError:
        return None
    return len(online_students)
