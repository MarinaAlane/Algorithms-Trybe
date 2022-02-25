# Função caseada no conteúdo do course https://app.betrybe.com/course/computer-
# science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-
# 216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-
# busca/bca54d30-feee-4326-aef4-278711fe9dcf?use_case=next_button
def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for entry_exit in permanence_period:
            if entry_exit[0] <= target_time <= entry_exit[1]:
                count += 1
    except TypeError:
        return None
    else:
        return count


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
