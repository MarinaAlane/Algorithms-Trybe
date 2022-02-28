def ordenate(string):
    s_list = list(string)
    for i in range(len(s_list)):
        minimum = i
        for j in range(i + 1, len(s_list)):
            if s_list[j] < s_list[minimum]:
                minimum = j
        s_list[minimum], s_list[i] = s_list[i], s_list[minimum]
    return s_list


def is_anagram(first_string, second_string):

    if ordenate(first_string) == ordenate(second_string):
        return True
    else:
        return False
