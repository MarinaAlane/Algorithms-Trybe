def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for x1, x2 in permanence_period:
            if x1 <= target_time <= x2:
                counter += 1
        return counter
    except TypeError:
        return None

if __name__ == '__main__':
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
