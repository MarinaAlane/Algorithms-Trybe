def study_schedule(permanence_period, target_time):
    c = 0
    for e, s in permanence_period:
      try:
          if e <= target_time <= s:
              c += 1
          return c
      except TypeError:
          return None
