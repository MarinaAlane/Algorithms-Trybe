def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    try:
        compatible_hours = 0
        for entry_time, departure_time in permanence_period:
            if entry_time <= target_time <= departure_time:
                compatible_hours += 1
        return compatible_hours
    except TypeError:
        return None
