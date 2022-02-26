# https://app.betrybe.com/course/computer-science/
# algoritmos/algoritmos-de-ordenacao-e-busca/29521083-
# 44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-
# 40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/
# fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
def string_to_list(string):
    data_list = list(string)
    new_list = list()
    for i in range(len(data_list)):
        minimum = min(data_list)
        new_list.append(minimum)
        data_list.remove(minimum)
    # for i in range(len(new_list)):
    #     min = i
    #     for j in range(i + 1, len(new_list)):
    #         if new_list[j] < new_list[min]:
    #             min = j
    #     new_list[min], new_list[i] = new_list[i], new_list[min]
    return new_list


def is_anagram(first_string, second_string):
    if string_to_list(first_string) == string_to_list(second_string):
        return True
    else:
        return False
