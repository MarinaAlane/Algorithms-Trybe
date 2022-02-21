def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None
    else:
        is_inside_target_time_count = 0
        for period in permanence_period:
            if isinstance(period[0], int) and isinstance(period[1], int):
                if period[0] <= target_time <= period[1]:
                    is_inside_target_time_count += 1
                else:
                    continue
            else:
                return None
        return is_inside_target_time_count
