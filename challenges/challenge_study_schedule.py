from collections import defaultdict


def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None
    period_dict = defaultdict(lambda:0)
    for initial, final in permanence_period:
        if not isinstance(initial, int) or not isinstance(final, int):
            return None
        for period in range(initial, final + 1):
            period_dict[period] += 1
    return period_dict[target_time]


# study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 3)