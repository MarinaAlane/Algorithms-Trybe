def study_schedule(permanence_period, target_time):
    cont = 0
    try:
        for p1, p2 in permanence_period:
            if p1 <= target_time <= p2:
                cont += 1
        return cont
    except TypeError:
        return None

if __name__ == '__main__':
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
